import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import injectContext from "./store/appContext.js";

import { Home } from "./pages/home.js";

import {LoginForm} from "./pages/components/loginForm.js";
import {RegisterForm} from "./pages/components/registerForm.js";


//create your first component
const Layout = () => {
	//the basename is used when your project is published in a subdirectory and not in the root of the domain
	// you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
	const basename = process.env.BASENAME || "";

	return (

			
			<BrowserRouter basename={basename} > 
					<Switch>
						<Route exact path="/">
							<Home />
						</Route>
						<Route exact path="/login">
							<LoginForm />
						</Route>
						<Route exact path="/register">
							<RegisterForm />
						</Route>
					</Switch>	
			</BrowserRouter>
		
	);
};

export default injectContext(Layout);