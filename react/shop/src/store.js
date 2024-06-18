import { configureStore, createSlice } from "@reduxjs/toolkit";
import user from "./store/userSlice";

const cart = createSlice({
  name: "cart",
  initialState: [
    { id: 0, name: "White and Black", count: 2 },
    { id: 2, name: "Grey Yordan", count: 1 },
  ],
  reducers: {
    addCount(state, action) {
      return state.map((item) =>
        item.id === action.payload ? { ...item, count: item.count + 1 } : item
      );
    },
    addItem(state, action) {
      state.push(action.payload);
    },
  },
});

export const { addCount, addItem } = cart.actions;

export default configureStore({
  reducer: {
    user: user.reducer,
    cart: cart.reducer,
  },
});
