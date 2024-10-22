import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
import HelloView from "@/views/HelloView"
import LoginView from "@/views/LoginView"
import NotFound404 from "@/views/NotFound404"
import DogView from "@/views/DogView"
import UploadTest from "@/views/UploadTest.vue"

Vue.use(VueRouter)

const isLoggedIn = true
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    // lazy-loading 방식 (첫 로딩에 렌더링하지 않고 해당 라우터가 동작할 때 컴포넌트를 렌더링한다)
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/hello/:userName",
    name: "hello",
    component: HelloView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log("Already Logged In!")
        next({ name: "home" })
      } else {
        next()
      }
    },
  },
  {
    path: "/404",
    name: "NotFound404",
    component: NotFound404,
  },
  {
    path: "/dog/:breed",
    name: "dog",
    component: DogView,
  },
  {
    path: "/test",
    name: "test",
    component: UploadTest,
  },
  {
    path: "*",
    redirect: "/404",
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

// router.beforeEach((to, from, next) => {
//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   // const authPages = ["hello", "home", "about"]
//   // 로그인이 필요하지 않은 페이지
//   const allowedPages = ["login"]

//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 사이트인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowedPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     console.log("Login으로 이동!")
//     next({ name: "login" })
//   } else {
//     console.log("to로 이동!")
//     next()
//   }
// })

export default router
