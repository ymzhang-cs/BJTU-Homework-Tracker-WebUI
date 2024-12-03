export interface Homework {
    courseName: string;
    title: string;
    submitStatus: string;
    createAt: string;
    openAt: string;
    dueAt: string;
}


interface PyWebviewApi {
    listAllHomework: () => Promise<Homework[]>;
    loginViaMis: () => Promise<void>;
    getLoginStatus: () => Promise<LoginStatus>;
}

class PyWebview {
    api: PyWebviewApi;
}

export declare const pywebview: PyWebview;
