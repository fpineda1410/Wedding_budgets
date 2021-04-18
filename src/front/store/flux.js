import React from "react";
import { Redirect } from "react-router";



const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {},
		actions: {}
	};
};

export default getState;