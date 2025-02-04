import pytest
from script.stack import Stack


@pytest.fixture(autouse=True)
def stack_instance() -> Stack:
    return Stack()


# Test creating a new stack
def test_create_stack(stack_instance):
    assert stack_instance.isEmpty() == True
    assert stack_instance.stack_size() == 0


# Test pushing items to the stack
def test_push(stack_instance):
    stack_instance.push(10)
    stack_instance.push(20)
    assert stack_instance.isEmpty() == False
    assert stack_instance.stack_size() == 2
    assert stack_instance.peek() == 20


# Test popping items from the stack
def test_pop(stack_instance):
    stack_instance.push(10)
    stack_instance.push(20)
    popped_value = stack_instance.pop()
    assert popped_value == 20
    assert stack_instance.stack_size() == 1
    assert stack_instance.peek() == 10

    # Test popping from an empty stack
    stack_instance.pop()
    assert stack_instance.isEmpty() == True
    assert stack_instance.stack_size() == 0
    assert stack_instance.pop() == "Stack is empty"


# Test peek on stack
def test_peek(stack_instance):
    stack_instance.push(10)
    stack_instance.push(20)
    assert stack_instance.peek() == 20  # Peek should return the top value
    stack_instance.pop()
    assert stack_instance.peek() == 10  # After popping, peek should return the new top


# Test isEmpty on stack
def test_is_empty(stack_instance):
    assert stack_instance.isEmpty() == True
    stack_instance.push(10)
    assert stack_instance.isEmpty() == False
    stack_instance.pop()
    assert stack_instance.isEmpty() == True


# Test stack size
def test_stack_size(stack_instance):
    assert stack_instance.stack_size() == 0
    stack_instance.push(10)
    assert stack_instance.stack_size() == 1
    stack_instance.push(20)
    assert stack_instance.stack_size() == 2
    stack_instance.pop()
    assert stack_instance.stack_size() == 1
