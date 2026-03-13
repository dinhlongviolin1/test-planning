"""
Tests for the dispatch_override module.

This test module verifies the functionality of the Dispatcher class
including registration, unregistration, dispatch, and override capabilities.
"""

import pytest
import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from dispatch_override import (
    Dispatcher,
    DispatchResult,
    HandlerNotFoundError,
    HandlerAlreadyExistsError,
    NoHandlersRegisteredError,
)


class TestDispatcherRegistration:
    """Tests for handler registration functionality."""

    def test_register_single_handler(self):
        """Test registering a single handler."""
        # Arrange
        dispatcher = Dispatcher()
        handler = lambda x: x * 2

        # Act
        dispatcher.register("double", handler)

        # Assert
        assert dispatcher.has_handler("double")
        assert dispatcher.get_handler("double") == handler

    def test_register_multiple_handlers(self):
        """Test registering multiple handlers."""
        # Arrange
        dispatcher = Dispatcher()
        handler1 = lambda x: x + 1
        handler2 = lambda x: x * 2

        # Act
        dispatcher.register("add_one", handler1)
        dispatcher.register("double", handler2)

        # Assert
        assert len(dispatcher.list_handlers()) == 2
        assert dispatcher.has_handler("add_one")
        assert dispatcher.has_handler("double")

    def test_register_duplicate_handler_raises_error(self):
        """Test that registering a duplicate handler raises an error."""
        # Arrange
        dispatcher = Dispatcher()
        handler1 = lambda x: x + 1
        handler2 = lambda x: x + 2

        # Act
        dispatcher.register("add", handler1)

        # Assert
        with pytest.raises(HandlerAlreadyExistsError) as exc_info:
            dispatcher.register("add", handler2)
        assert "already registered" in str(exc_info.value).lower()


class TestDispatcherUnregistration:
    """Tests for handler unregistration functionality."""

    def test_unregister_existing_handler(self):
        """Test unregistering an existing handler."""
        # Arrange
        dispatcher = Dispatcher()
        handler = lambda x: x * 2
        dispatcher.register("double", handler)

        # Act
        dispatcher.unregister("double")

        # Assert
        assert not dispatcher.has_handler("double")
        assert len(dispatcher.list_handlers()) == 0

    def test_unregister_nonexistent_handler_raises_error(self):
        """Test that unregistering a non-existent handler raises an error."""
        # Arrange
        dispatcher = Dispatcher()

        # Assert
        with pytest.raises(HandlerNotFoundError) as exc_info:
            dispatcher.unregister("nonexistent")
        assert "not registered" in str(exc_info.value).lower()


class TestDispatcherDispatch:
    """Tests for dispatch functionality."""

    def test_dispatch_simple_handler(self):
        """Test dispatching a simple handler."""
        # Arrange
        dispatcher = Dispatcher()
        handler = lambda x: x * 2
        dispatcher.register("double", handler)

        # Act
        result = dispatcher.dispatch("double", 5)

        # Assert
        assert result.success is True
        assert result.result == 10
        assert result.handler_name == "double"

    def test_dispatch_with_args_and_kwargs(self):
        """Test dispatching a handler with positional and keyword arguments."""
        # Arrange
        dispatcher = Dispatcher()
        def handler(a, b, c=1):
            return a + b + c
        dispatcher.register("add", handler)

        # Act
        result = dispatcher.dispatch("add", 1, 2, c=3)

        # Assert
        assert result.success is True
        assert result.result == 6

    def test_dispatch_nonexistent_handler_raises_error(self):
        """Test that dispatching a non-existent handler raises an error."""
        # Arrange
        dispatcher = Dispatcher()
        dispatcher.register("existing", lambda x: x)

        # Assert
        with pytest.raises(HandlerNotFoundError):
            dispatcher.dispatch("nonexistent")

    def test_dispatch_with_no_handlers_raises_error(self):
        """Test that dispatching with no registered handlers raises an error."""
        # Arrange
        dispatcher = Dispatcher()

        # Assert
        with pytest.raises(NoHandlersRegisteredError):
            dispatcher.dispatch("any_handler")

    def test_dispatch_returns_error_result_on_exception(self):
        """Test that dispatch returns error result when handler raises exception."""
        # Arrange
        dispatcher = Dispatcher()
        def failing_handler():
            raise ValueError("Test error")
        dispatcher.register("fail", failing_handler)

        # Act
        result = dispatcher.dispatch("fail")

        # Assert
        assert result.success is False
        assert result.error == "Test error"
        assert result.handler_name == "fail"


class TestDispatcherOverride:
    """Tests for handler override functionality."""

    def test_override_existing_handler(self):
        """Test overriding an existing handler."""
        # Arrange
        dispatcher = Dispatcher()
        original_handler = lambda x: x + 1
        new_handler = lambda x: x + 10
        dispatcher.register("add", original_handler)

        # Act
        dispatcher.override("add", new_handler)

        # Assert
        assert dispatcher.has_handler("add")
        result = dispatcher.dispatch("add", 5)
        assert result.result == 15

    def test_override_nonexistent_handler_registers_new(self):
        """Test that overriding a non-existent handler registers a new one."""
        # Arrange
        dispatcher = Dispatcher()
        new_handler = lambda x: x * 3

        # Act
        dispatcher.override("triple", new_handler)

        # Assert
        assert dispatcher.has_handler("triple")
        result = dispatcher.dispatch("triple", 5)
        assert result.result == 15


class TestDispatcherEdgeCases:
    """Tests for edge cases in the Dispatcher class."""

    def test_list_handlers_empty(self):
        """Test listing handlers when none are registered."""
        # Arrange
        dispatcher = Dispatcher()

        # Act & Assert
        assert dispatcher.list_handlers() == []

    def test_list_handlers_after_operations(self):
        """Test listing handlers after various operations."""
        # Arrange
        dispatcher = Dispatcher()
        dispatcher.register("a", lambda: 1)
        dispatcher.register("b", lambda: 2)

        # Act
        handlers = dispatcher.list_handlers()

        # Assert
        assert len(handlers) == 2
        assert "a" in handlers
        assert "b" in handlers

        # Act - after unregister
        dispatcher.unregister("a")
        handlers = dispatcher.list_handlers()

        # Assert
        assert len(handlers) == 1
        assert "a" not in handlers

    def test_get_handler_returns_none_for_missing(self):
        """Test that get_handler returns None for non-existent handlers."""
        # Arrange
        dispatcher = Dispatcher()

        # Act & Assert
        assert dispatcher.get_handler("missing") is None

    def test_has_handler_returns_correct_value(self):
        """Test has_handler returns correct boolean value."""
        # Arrange
        dispatcher = Dispatcher()
        dispatcher.register("exists", lambda: 1)

        # Act & Assert
        assert dispatcher.has_handler("exists") is True
        assert dispatcher.has_handler("does_not_exist") is False