import { useQuery } from "@tanstack/react-query";
import { fetchComments } from "./api";
import "./PostDetail.css";

export function PostDetail({ post, deleteMutation, updateMutation }) {
  // replace with useQuery
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["comments", post.id],
    queryFn: () => fetchComments(post.id),
  });
  if (isLoading) return <div>로딩중</div>;
  if (isError)
    return (
      <>
        <div>에러뜸</div>
        <p>{error.toString()}</p>
      </>
    );

  return (
    <>
      <h3 style={{ color: "blue" }}>{post.title}</h3>
      <div>
        <button onClick={() => deleteMutation.mutate(post.id)}>Delete</button>
        {deleteMutation.isPending && <p className="loading">지우는 중</p>}
        {deleteMutation.isError && (
          <p className="error">
            포스트 삭제 중 에러: {deleteMutation.error.toString()}
          </p>
        )}
        {deleteMutation.isSuccess && (
          <p className="success">Post was (not) deleted</p>
        )}
      </div>
      <div>
        <button onClick={() => updateMutation.mutate(post.id)}>
          Update title
        </button>
        {updateMutation.isPending && <p className="loading">업데이트 중</p>}
        {updateMutation.isError && (
          <p className="error">
            포스트 업데이트 중 에러:{updateMutation.error.toString()}
          </p>
        )}
        {updateMutation.isSuccess && <p className="success">업데이트 성공</p>}
      </div>
      <p>{post.body}</p>
      <h4>Comments</h4>
      {data.map((comment) => (
        <li key={comment.id}>
          {comment.email}: {comment.body}
        </li>
      ))}
    </>
  );
}
