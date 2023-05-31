import Vue from "vue"
import VueRouter from "vue-router"
import TheLunch from "@/views/TheLunch"
import TheLotto from "@/views/TheLotto"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "TheLunch",
    component: TheLunch,
  },
  {
    path: "/lotto/:menu",
    name: "TheLotto",
    component: TheLotto,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
