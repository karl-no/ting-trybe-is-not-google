from ting_file_management.priority_queue import PriorityQueue
import pytest

priority_file = {"qtd_linhas": 3}
non_priority_file = {"qtd_linhas": 6}


def test_basic_priority_queueing():
    priority = PriorityQueue()

    priority.enqueue(non_priority_file)
    assert priority.dequeue() == non_priority_file

    priority.enqueue(non_priority_file)
    priority.enqueue(priority_file)
    assert priority.search(0) == priority_file

    with pytest.raises(IndexError):
        priority.search(7)
