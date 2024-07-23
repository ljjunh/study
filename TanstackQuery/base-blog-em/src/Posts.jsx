import { useState, useEffect } from "react";
import { useQuery, useQueryClient, useMutation } from "@tanstack/react-query";
import { fetchPosts, deletePost, updatePost } from "./api";
import { PostDetail } from "./PostDetail";
const maxPostPage = 10;

export function Posts() {
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedPost, setSelectedPost] = useState(null);

  const queryClient = useQueryClient();

  // 이미 useQuery에서 반환 객체를 구조분해 했기 때문에 변수명 복잡해지니까 여기선 구조분해할당 안씀
  const deleteMutation = useMutation({
    // 쿼리 키가 필요 없음. 캐시 데이터랑 관련 없기 때문
    mutationFn: (postId) => deletePost(postId),
  });

  // deleteMutation.mutate

  const updateMutation = useMutation({
    mutationFn: (postId) => updatePost(postId),
  });

  useEffect(() => {
    if (currentPage < maxPostPage) {
      const nextPage = currentPage + 1;
      queryClient.prefetchQuery({
        queryKey: ["posts", nextPage],
        queryFn: () => fetchPosts(nextPage),
      });
    }
  }, [currentPage, queryClient]);

  // 쿼리키: 항상 배열
  const { data, isError, error, isLoading } = useQuery({
    queryKey: ["posts", currentPage],
    queryFn: () => fetchPosts(currentPage),
    staleTime: 2000,
  });
  if (isLoading) {
    return <h3>로딩중</h3>;
  }
  if (isError) {
    return (
      <>
        <h3>에러가 발생함</h3>
        <p>{error.toString()}</p>
      </>
    );
  }

  return (
    <>
      <ul>
        {data.map((post) => (
          <li
            key={post.id}
            className="post-title"
            onClick={() => {
              deleteMutation.reset();
              updateMutation.reset();
              setSelectedPost(post);
            }}
          >
            {post.title}
          </li>
        ))}
      </ul>
      <div className="pages">
        <button
          disabled={currentPage <= 1}
          onClick={() => {
            setCurrentPage((previousValue) => previousValue - 1);
          }}
        >
          Previous page
        </button>
        <span>Page {currentPage}</span>
        <button
          disabled={currentPage >= maxPostPage}
          onClick={() => {
            setCurrentPage((previousValue) => previousValue + 1);
          }}
        >
          Next page
        </button>
      </div>
      <hr />
      {selectedPost && (
        <PostDetail
          post={selectedPost}
          deleteMutation={deleteMutation}
          updateMutation={updateMutation}
        />
      )}
    </>
  );
}
