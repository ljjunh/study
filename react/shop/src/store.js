import { configureStore, createSlice } from "@reduxjs/toolkit";
import user from "./store/userSlice";
// Redux 왜씀?
// 컴포넌트간 state 공유 편해짐
// props 전송이 필요 없음
// state 하나를 slice라고 부름
// const 작명 = createSlice({
//   name: "작명",
//   initialState: "값"
// })

// redux안의 state 수정하는 법
// 1.state 수정해주는 함수 만들기
// 2. 만든 함수 export
// 3. 만든 함수 import 해서 사용
const cartData = createSlice({
  name: "cartData",
  initialState: [
    { id: 0, name: "White and Black", count: 2 },
    { id: 2, name: "Grey Yordan", count: 1 },
  ],
  reducers: {
    addCount(state, action) {
      const num = state.findIndex((item) => {
        return item.id === action.payload;
      });
      state[num].count += 1;
    },
    addItem(state, action) {
      state.push(action.payload);
    },
  },
});
export let { addCount, addItem } = cartData.actions;

export default configureStore({
  reducer: {
    //여기에 등록해야 사용 가능
    // user: user.reducer, 뒤에 reducer 붙여야함
    cartData: cartData.reducer,
    user: user.reducer,
  },
});
