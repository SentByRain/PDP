import type { AxiosError, AxiosInstance, AxiosResponse } from "axios";

import type { registrationInfo } from "@/interfaces/reg&auth";
import axios from "axios";

export async function requestVerificationCode(
  requestBase: AxiosInstance,
  store: registrationInfo
) {
  try {
    const resp = await requestBase.post(
      "/mail/send_verification_code?email=" + store.email
    );
    return resp;
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      // it's AxiosError type
      console.error("Axios error:", error.response?.data.message);
    } else {
      // it's different error
      console.error("Unexpected error:", error);
    }
  }
}

export async function sendUserInfo(
  requestBase: AxiosInstance,
  store: registrationInfo
) {
  const userInfo: Object = {
    role: store.role,
    name: store.username,
    surname: store.surname,
    email: store.email,
    password: store.password,
    verification_code: store.enteredCode,
  };
  try {
    const resp = await requestBase.post("/users/register", userInfo);
    return resp;
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      // it's AxiosError type
      console.error("Axios error:", error.response?.data.message);
    } else {
      // it's different error
      console.error("Unexpected error:", error);
    }
  }
}

export async function sendAuthInfo(
  requestBase: AxiosInstance,
  email: string,
  password: string
) {
  const userInfo: Object = {
    email: email,
    password: password,
  };
  try {
    const resp = await requestBase.post("/users/login", userInfo);
    return resp;
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      // it's AxiosError type
      console.error("Axios error:", error.response?.data.message);
    } else {
      // it's different error
      console.error("Unexpected error:", error);
    }
    // console.log(error.response.data.message);
  }
}
export default function (instance: AxiosInstance) {
  return {};
}
