import type { AxiosError, AxiosInstance } from "axios";

import type { registrationInfo } from "@/interfaces/reg&auth";

export async function requestVerificationCode(
  requestBase: AxiosInstance,
  store: registrationInfo
) {
  const resp = await requestBase.post(
    "/mail/send_verification_code?email=" + store.email
  );
  return resp;
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
  // добавить try catch
  const resp = await requestBase.post("/users/register", userInfo);
  return resp;
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
  } catch (e) {
    // подшаманить с typescript
    console.log(e.status);
  }
}
export default function (instance: AxiosInstance) {
  return {};
}
