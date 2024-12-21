import axios from "axios";
import type { AxiosError, AxiosInstance, AxiosResponse } from "axios";

const requestBase: AxiosInstance = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    Accept: "application/json",
    "Content-type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});

export default requestBase;
