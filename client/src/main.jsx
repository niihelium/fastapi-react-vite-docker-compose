import * as React from "react";
import { createRoot } from 'react-dom/client';
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";

import Home from './Home';
import Greet from './Greet';

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
    },{
        path: "/greet",
        element: <Greet />
    }

]);

// Render your React component instead
createRoot(document.getElementById('app'))
    .render(
        <React.StrictMode>
            <RouterProvider router={router} />
        </React.StrictMode>
    );