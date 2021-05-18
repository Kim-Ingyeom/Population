# Population
주제: 지역별 인구수 통계



프로젝트 내용:

지역별 인구수 통계를 나타내는 사이트에서 지역별 인구수의 증감을 나타내는 그래프를 나타내려 한다.

구체적으로 지역이름과 현 인구수 그리고 인구수 변화정도를 크롤링한다. 지역이름과 현 인구수를 그래프 1, 지역이름과 인구수 변화율을 그래프 2로 matplotlib를 이용해 표기한다.

단, 이 때 나타낼 지역은 상위 5지역으로만 한다.



202155125 김인겸 역할

크롤링 - 사이트에서 제공하는 지역이름과 그 지역의 현 인구수를 Selenium을 이용해 전체 테이블을 찾아서 반환한다.

그래프 - 지역이름을 X축 그 지역의 인구수를 Y축으로 하는 그래프 코드를 작성한다.



202155140 박재형 역할

크롤링 - 사이트에서 제공하는 지역이름과 그 지역의 인구수 변화정도를 Selenium을 이용해 전체 테이블을 찾아서 반환한다.

그래프 - 지역이름을 X축 그 지역의 인구수 변화 정도를 Y축으로 하는 그래프 코드를 김인겸이 작성한 그래프에 덧씌운다





크롤링할 사이트 URL: 지역별 인구수 통계 (2021년 4월) (superkts.com)
