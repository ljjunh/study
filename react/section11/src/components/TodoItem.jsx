import "./TodoItem.css";
import { memo, useContext } from "react";
import { TodoDispatchContext } from "../App";
const TodoItem = ({ id, isDone, content, date }) => {
  const { onUpdate, onDelete } = useContext(TodoDispatchContext);
  const onChangeCheckbox = () => {
    onUpdate(id);
  };
  const onClickDeleteButton = () => {
    onDelete(id);
  };
  return (
    <div className="TodoItem">
      <input
        onChange={onChangeCheckbox}
        type="checkbox"
        checked={isDone}
        readOnly
      />
      <div className="content">{content}</div>
      <div className="date">{new Date(date).toLocaleDateString()}</div>
      <button onClick={onClickDeleteButton}>삭제</button>
    </div>
  );
};

// 고차 컴포넌트 (HOC)
// export default memo(TodoItem, (prevProps, nextProps) => {
//   // 반환값에 따라 , props가 바뀌었는지 판단
//   // T => Props 바뀌지 않음 -> 리렌더링x
//   // F => Props 바뀜 -> 리렌더링o
//   if (prevProps.id !== nextProps.id) return false;
//   if (prevProps.isDone !== nextProps.isDone) return false;
//   if (prevProps.content !== nextProps.content) return false;
//   if (prevProps.date !== nextProps.date) return false;
//   // 만약 아무것도 안바뀌면 true반환해서 리렌더링 되지 않도록
//   return true;
// });
export default memo(TodoItem);
