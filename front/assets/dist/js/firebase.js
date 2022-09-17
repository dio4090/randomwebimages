// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.4/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.9.4/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAyvwBPFLbRny4DZQ4uxCSUADUHzpuVWw4",
    authDomain: "randomwebimages-493ec.firebaseapp.com",
    projectId: "randomwebimages-493ec",
    storageBucket: "randomwebimages-493ec.appspot.com",
    messagingSenderId: "527525187459",
    appId: "1:527525187459:web:a7b6f5378d1e3f3585f0b6",
    measurementId: "G-S0YM9QFQFP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);