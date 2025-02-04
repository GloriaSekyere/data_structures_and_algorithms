import pytest
from script.queue import Queue


@pytest.fixture(autouse=True)
def queue_instance() -> Queue:
    return Queue()


# Test creating a new queue
def test_create_queue(queue_instance):
    assert queue_instance.isEmpty() == True
    assert queue_instance.queue_size() == 0


# Test enqueuing items to the queue
def test_enqueue(queue_instance):
    queue_instance.enqueue(10)
    queue_instance.enqueue(20)
    assert queue_instance.isEmpty() == False
    assert queue_instance.queue_size() == 2
    assert queue_instance.peek() == 10


# Test dequeuing items from the queue
def test_dequeue(queue_instance):
    queue_instance.enqueue(10)
    queue_instance.enqueue(20)
    dequeued_value = queue_instance.dequeue()
    assert dequeued_value == 10
    assert queue_instance.queue_size() == 1
    assert queue_instance.peek() == 20

    # Test dequeuing from an empty queue
    queue_instance.dequeue()
    assert queue_instance.isEmpty() == True
    assert queue_instance.queue_size() == 0
    assert queue_instance.dequeue() == "Queue is empty"


# Test peek on queue
def test_peek(queue_instance):
    queue_instance.enqueue(10)
    queue_instance.enqueue(20)
    assert queue_instance.peek() == 10  # Peek should return the front value
    queue_instance.dequeue()
    assert (
        queue_instance.peek() == 20
    )  # After dequeuing, peek should return the new front


# Test isEmpty on queue
def test_is_empty(queue_instance):
    assert queue_instance.isEmpty() == True
    queue_instance.enqueue(10)
    assert queue_instance.isEmpty() == False
    queue_instance.dequeue()
    assert queue_instance.isEmpty() == True


# Test queue size
def test_queue_size(queue_instance):
    assert queue_instance.queue_size() == 0
    queue_instance.enqueue(10)
    assert queue_instance.queue_size() == 1
    queue_instance.enqueue(20)
    assert queue_instance.queue_size() == 2
    queue_instance.dequeue()
    assert queue_instance.queue_size() == 1
