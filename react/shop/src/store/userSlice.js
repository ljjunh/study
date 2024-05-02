import { createSlice } from "@reduxjs/toolkit";

const user = createSlice({
  name: "user",
  initialState: { name: "kim", age: 20 },
  reducers: {
    changeName(state) {
      //array/object의 경우 return 안쓰고 직접 수정해도 됨
      state.name = "park";
    },
    increase(state, action) {
      state.age += action.payload; //화물 보낸거 쓰려면 payload
    },
  },
});
export let { changeName, increase } = user.actions;
export default user;
