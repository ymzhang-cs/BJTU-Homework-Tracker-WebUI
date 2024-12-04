export interface Homework {
    courseName: string;
    title: string;
    submitStatus: string;
    createAt: string;
    openAt: string;
    dueAt: string;
}


interface PyWebviewApi {
    listAllHomework(): Promise<Homework[]>;
    loginViaMis(): Promise<void>;
    loginViaCookies(cookies: string): Promise<void>;
    loginViaCoursePlatform(account: string, password: string): Promise<void>;
    getLoginStatus(): Promise<LoginStatus>;
    logout(): Promise<void>;
}

class PyWebview {
    api: PyWebviewApi;
}

export declare global {
    const pywebview: PyWebview;
}

