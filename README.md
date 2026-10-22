# 폴더 크기 시각화 예제

[폴더 크기 분석기](https://github.com/JimProKing/Measuring-folder-size-Program_Python)에서 계산한 폴더별 용량을 가로 막대그래프로 그리는 예제입니다.

| 분류 | 상태 | 스택 | 바로 보기 |
| --- | --- | --- | --- |
| 데이터 · 시각화 | 완료 | Python · matplotlib · numpy | — |

## 구성

| 파일 | 하는 일 |
| --- | --- |
| `step3_1.py` | 폴더별 크기를 `{폴더명: 크기}` JSON으로 저장 (`dump_plot_data`, `load_plot_data`) |
| `step3_2.py` | 기본 가로 막대그래프 → `output/step3_2.png` |
| `step3_3.py` | 로그 스케일 막대그래프. 폴더 크기 차이가 클 때 |
| `step3_폴더목록JSON.py` · `step4_폴더크기측정실행.py` | 분석기에서 가져온 데이터 생성 단계 |

## 실행

```bash
python step4_폴더크기측정실행.py   # 폴더 크기 데이터 만들기
python step3_1.py                  # JSON 저장
python step3_2.py                  # 그래프
```

`fig, ax = plt.subplots()` 후 `ax.barh()`로 그리고, 결과는 `output/`에 저장됩니다.

---

**관련 저장소** · [Measuring-folder-size-Program_Python](https://github.com/JimProKing/Measuring-folder-size-Program_Python) · [Card_Log_Practice](https://github.com/JimProKing/Card_Log_Practice)

<sub>[JimProKing](https://github.com/JimProKing) · 이영찬 — 전체 저장소는 프로필의 프로젝트 지도에서 분야별로 볼 수 있습니다.</sub>
<!-- jpk-footer -->
