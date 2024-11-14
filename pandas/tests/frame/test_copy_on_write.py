import pytest
import pandas as pd

def test_copy_on_write_broadcasting():
    # Copy-on-Write 모드 활성화
    pd.options.mode.copy_on_write = True

    # 테스트할 데이터프레임 생성
    dftest = pd.DataFrame({"A": [1, 4, 1, 5], "B": [2, 5, 2, 6], "C": [3, 6, 1, 7]})
    df = dftest[["B", "C"]]

    try:
        # broadcasting이 발생하지 않도록 값 할당
        df.iloc[[1, 3], :] = [[2, 2], [2, 2]]
    except ValueError:
        pytest.fail("Broadcasting issue not resolved in Copy-on-Write mode")
    
    # 결과 확인
    assert df.iloc[1, 0] == 2
    assert df.iloc[3, 0] == 2
    assert df.iloc[1, 1] == 2
    assert df.iloc[3, 1] == 2
