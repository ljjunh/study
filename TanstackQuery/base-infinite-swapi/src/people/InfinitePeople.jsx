import InfiniteScroll from "react-infinite-scroller";
import { useInfiniteQuery } from "@tanstack/react-query";
import { Person } from "./Person";

// Star Wars API의 초기 URL을 정의. 이 URL 에서 첫 페이지의 데이터를 가져올거임
const initialUrl = "https://swapi.dev/api/people/";

// 주어진 URL에서 데이터를 가져오는 비동기 함수
const fetchUrl = async (url) => {
  const response = await fetch(url);
  return response.json();
};

export function InfinitePeople() {
  const {
    data, // 가져온 데이터
    fetchNextPage, // 다음 페이지 데이터를 가져오는 함수
    hasNextPage, // 다음 페이지가 있는지 여부 getNextPageParam 함수의 반환값에 따라 결정
    isFetching, // 데이터를 가져오는 중인지 여부
    isLoading, // 초기 로딩 중인지 여부
    isError, // 에러가 발생했는지 여부
    error, // 발생한 에러 객체
  } = useInfiniteQuery({
    // 쿼리의 고유 키 정의
    queryKey: ["sw-people"],
    // 데이터를 가져오는 함수. pageParam이 없으면 initialUrl을 사용
    // 초기 호출시에는 pageParam이 없으니까 지정한 initialUrl을 디폴트 값으로 지정
    // 이후 호출에서는 getNextPageParam에서 반환된 값이 pageParam으로 사용됨
    queryFn: ({ pageParam = initialUrl }) => fetchUrl(pageParam),

    // 다음 페이지의 URL을 결정하는 함수. API응답의 next필드를 사용
    getNextPageParam: (lastPage) => {
      // lastPage : queryFn에서 반환된 데이터로 가장 최근에 가져온 페이지의 데이터
      return lastPage.next || undefined;
      // queryFn에서 반환된 lastPage의 next필드가 존재하면(즉, 다음페이지가 있으면) 이 값을 반환해서 다음 queryFn 호출의 pageParamd으로 사용
      // queryFn에서 반환된 lastPage의 next필드가 없으면(즉, 마지막 페이지라면) undefined를 반환
    },
  });

  // 초기 로딩 중일 때 로딩 메세지를 표시
  if (isLoading) {
    return <div className="loading">로딩중...</div>;
  }
  // 에러가 발생했을 때 에러 메시지를 표시
  if (isError) {
    return <div>에러 : {error.toString()}</div>;
  }
  // 데이터가 로드되면 InfiniteScroll 컴포넌트를 사용해서 데이터 표시
  return (
    <>
      {/* ux를 향상시키기 위해 사용 isFetching은 초기 로딩 이후에도 추가 데이터를 가져오는 중일때 true가 되서 */}
      {/* isLoading은 쿼리가 처음 실행될때만 true가 됨. 한번 데이터를 가져오면 스크롤을 내려 추가 데이터를 요청해도 false 상태를 유지해서 사용자가 이후 요청할때 로딩중이라는걸 못봄*/}
      {/* isFetching은 쿼리가 데이터를 가져올때마다 true가 됨. 데이터를 가져오면 false로 됐다가 스크롤을 내려 추가 데이터를 요청할 때마다 true로 변경. 그래서 사용자가 스크롤을 내릴때마다 로딩중이라는걸 알 수 있음*/}
      {isFetching && <div className="loading">로딩중...</div>}
      <InfiniteScroll
        initialLoad={false} // 컴포넌트 마운트 시 자동으로 데이터를 로드하지 않음
        loadMore={() => {
          // 현재 데이터를 가져오는 중이 아닐 때만 다음 페이지를 로드
          if (!isFetching) {
            fetchNextPage(); // useInfiniteQuery 반환값 fetchNextPage를 실행
          }
        }}
        hasMore={hasNextPage} // 더 로드할 데이터가 있는지 여부 useInfiniteQuery의 반환값 hasNextPage를 사용
      >
        {data.pages.map((pageData) => {
          return pageData.results.map((person) => {
            return (
              <Person
                key={person.name}
                name={person.name}
                hairColor={person.hair_color}
                eyeColor={person.eye_color}
              />
            );
          });
        })}
      </InfiniteScroll>
    </>
  );
}
