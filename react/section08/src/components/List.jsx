import "./List.css";
import TodoItem from "./TodoItem";
import { useState } from "react";
const List = ({ todos }) => {
  const [search, setSearch] = useState("");
  const onChangeSearch = (e) => {
    setSearch(e.target.value);
  };
  const getSearchResult = () => {
    return search === ""
      ? todos
      : todos.filter((item) => {
          return item.content.toLowerCase().includes(search.toLowerCase());
        });
  };
  return (
    <div className="List">
      <h4>Todo List🌱</h4>
      <input
        value={search}
        onChange={onChangeSearch}
        placeholder="검색어를 입력하세요"
      />
      <div className="todos_wrapper"></div>
      {getSearchResult().map((item) => {
        return <TodoItem key={item.id} {...item} />;
      })}
    </div>
  );
};
export default List;
