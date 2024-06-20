import { useSelector, useDispatch } from "react-redux";
import { setTitle } from "./bookSlice";
const BookItem = () => {
  const title = useSelector((state) => state.book.title);
  const dispatch = useDispatch();

  return (
    <div>
      <h4>책목록</h4>
      <p>{title}</p>
      <button
        onClick={() => {
          dispatch(setTitle("신데렐라"));
        }}
      >
        클릭
      </button>
    </div>
  );
};

export default BookItem;
