"""
Dispatch Override Module

This module provides a Dispatcher class with support for handler registration,
unregistration, dispatching, and override capability.
"""

from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass


class DispatcherError(Exception):
    """Base exception for Dispatcher errors."""
    pass


class HandlerNotFoundError(DispatcherError):
    """Raised when a handler is not found."""
    pass


class HandlerAlreadyExistsError(DispatcherError):
    """Raised when trying to register a handler that already exists."""
    pass


class NoHandlersRegisteredError(DispatcherError):
    """Raised when dispatch is called with no handlers registered."""
    pass


@dataclass
class DispatchResult:
    """Represents the result of a dispatch operation."""
    handler_name: str
    success: bool
    result: Any
    error: Optional[str] = None


class Dispatcher:
    """
    A dispatcher class that supports handler registration, unregistration,
    dispatching, and handler override capability.

    Attributes:
        _handlers: Dictionary mapping handler names to handler functions
    """

    def __init__(self) -> None:
        """Initialize the Dispatcher with an empty handler registry."""
        self._handlers: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, handler: Callable[..., Any]) -> None:
        """
        Register a new handler.

        Args:
            name: The name of the handler
            handler: The handler function to register

        Raises:
            HandlerAlreadyExistsError: If a handler with this name already exists
        """
        if name in self._handlers:
            raise HandlerAlreadyExistsError(
                f"Handler '{name}' is already registered. "
                f"Use override() to replace an existing handler."
            )
        self._handlers[name] = handler

    def unregister(self, name: str) -> None:
        """
        Unregister a handler.

        Args:
            name: The name of the handler to unregister

        Raises:
            HandlerNotFoundError: If no handler with this name is registered
        """
        if name not in self._handlers:
            raise HandlerNotFoundError(
                f"Handler '{name}' is not registered."
            )
        del self._handlers[name]

    def override(self, name: str, handler: Callable[..., Any]) -> None:
        """
        Override an existing handler with a new one.

        If the handler doesn't exist, it will be registered.

        Args:
            name: The name of the handler to override
            handler: The new handler function
        """
        self._handlers[name] = handler

    def dispatch(self, name: str, *args: Any, **kwargs: Any) -> DispatchResult:
        """
        Dispatch a call to a specific handler.

        Args:
            name: The name of the handler to call
            *args: Positional arguments to pass to the handler
            **kwargs: Keyword arguments to pass to the handler

        Returns:
            DispatchResult with the handler name, success status, result, and optional error

        Raises:
            NoHandlersRegisteredError: If no handlers are registered
        """
        if not self._handlers:
            raise NoHandlersRegisteredError(
                "No handlers are registered. Cannot dispatch."
            )

        if name not in self._handlers:
            raise HandlerNotFoundError(
                f"Handler '{name}' is not registered."
            )

        try:
            result = self._handlers[name](*args, **kwargs)
            return DispatchResult(
                handler_name=name,
                success=True,
                result=result
            )
        except Exception as e:
            return DispatchResult(
                handler_name=name,
                success=False,
                result=None,
                error=str(e)
            )

    def get_handler(self, name: str) -> Optional[Callable[..., Any]]:
        """
        Get a handler by name.

        Args:
            name: The name of the handler

        Returns:
            The handler function if found, None otherwise
        """
        return self._handlers.get(name)

    def list_handlers(self) -> List[str]:
        """
        List all registered handler names.

        Returns:
            List of handler names
        """
        return list(self._handlers.keys())

    def has_handler(self, name: str) -> bool:
        """
        Check if a handler is registered.

        Args:
            name: The name of the handler

        Returns:
            True if the handler is registered, False otherwise
        """
        return name in self._handlers


# Module-level dispatcher instance for convenience
_default_dispatcher: Optional[Dispatcher] = None


def get_dispatcher() -> Dispatcher:
    """
    Get the default dispatcher instance.

    Returns:
        The default Dispatcher instance
    """
    global _default_dispatcher
    if _default_dispatcher is None:
        _default_dispatcher = Dispatcher()
    return _default_dispatcher