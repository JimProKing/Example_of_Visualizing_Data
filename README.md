Markdown# 폴더 크기 시각화 예제

`폴더 크기 측정` 프로젝트에서 계산한 각 폴더(디렉터리)의 크기를  
**가로 막대그래프**로 예쁘게 그려주는 간단한 데이터 시각화 예제입니다.

## 프로젝트 구조 (핵심 파일만)
.
├─ 폴더 크기 측정/
│   ├─ step1_폴더생성.py          # OUT_DIR 정의
│   └─ step4_폴더크기측정실행.py # load_filesize_per_dir() 함수
└─ 데이터시각화_예제/
├─ step3_1.py                 # JSON 저장용 (dump_plot_data)
├─ step3_2.py                 # 기본 가로 막대그래프
└─ step3_3_log.py             # 로그 스케일 가로 막대그래프
text## 실행 방법

1. **먼저 폴더 크기 측정**  
   `폴더 크기 측정/step4_폴더크기측정실행.py` 를 실행해서 폴더별 크기 데이터를 만든다.

2. **JSON 데이터 생성**  
   ```bash
   python "데이터시각화_예제/step3_1.py"
→ output/plot_data.json (또는 step3_1.json) 파일이 생성됩니다.

그래프 그리기
기본 가로 막대그래프Bashpython "데이터시각화_예제/step3_2.py"→ output/step3_2.png
로그 스케일 그래프 (크기 차이가 큰 경우 추천)Bashpython "데이터시각화_예제/step3_3_log.py"→ output/step3_3_log.png


코드 설명
step3_1.py – JSON 저장
Python# 폴더별 크기를 {폴더명: 크기} 형태로 정리해서 JSON으로 저장
dump_plot_data()   # 실행하면 OUT_DIR에 *.json 파일 생성
load_plot_data()   # 나중에 그래프 그릴 때 재사용
step3_2.py – 기본 가로 막대그래프
Pythonfig, ax = plt.subplots()           # ← subplots (s 꼭 붙이기!)
ax.barh(stems, sizes)              # 가로 막대그래프
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")
step3_3_log.py – 로그 스케일 그래프
크기가 천차만별일 때 눈에 잘 들어오는 로그 스케일 버전입니다.
Pythonlog_size = np.log(plot_data["size"])
ax.barh(plot_data["stem"], log_size)