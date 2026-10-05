def test_smoke():
    from lambdawalker.process.process_in_parrallel import process_parallel
    assert process_parallel is not None
    print("process OK")
