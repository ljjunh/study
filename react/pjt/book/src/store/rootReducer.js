import { combineReducers } from "@reduxjs/toolkit";
import bookSlice from "../features/book/bookSlice";

const rootReducer = combineReducers({
  book: bookSlice,
});

export default rootReducer;
