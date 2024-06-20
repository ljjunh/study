import { createSlice } from "@reduxjs/toolkit";

const bookSlice = createSlice({
  name: "book",
  initialState: {
    title: "어린 왕자",
  },
  reducers: {
    setTitle(state, action) {
      console.log(state);
      console.log(action);
      state.title = action.payload;
    },
  },
});

export const { setTitle } = bookSlice.actions;
export default bookSlice.reducer;
