import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

import axios from "axios"
const API_KEY = "9dafc716aecd5cd988912f43b852ab6c"
const OPENWEATHERMAP_API_KEY = "9bb607c5051f148d38ced029dd8953fd"
const TOP_RATED_URL = "https://api.themoviedb.org/3/movie/top_rated"
const CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

export default new Vuex.Store({
  state: {
    movieCards: [],
    watchList: [],
    currentWeather: null,
  },
  getters: {},
  mutations: {
    LOAD_MOVIE_CARDS(state, response) {
      state.movieCards = response
    },
    LOAD_CURRENT_WEATHER(state, response) {
      state.currentWeather = response
    },
    CREATE_WATCH_LIST(state, item) {
      console.log("CREATE_WATCH_LIST __________________________________")
      state.watchList.push(item)
    },
    UPDATED_WATCH_LIST(state, item) {
      // console.log(item)
      state.watchList = state.watchList.map((list) => {
        if (list === item) {
          list.isCompleted = !list.isCompleted
        }
        return list
      })
    },
    LOAD_LIST(state) {
      const localStorageList = localStorage.getItem("list")
      const parsedList = JSON.parse(localStorageList)
      state.watchList = parsedList
    },
    DELETE_LIST(state, list) {
      const index = state.watchList.indexOf(list)
      state.watchList.splice(index, 1)
    },
  },
  actions: {
    loadMovieCards(context) {
      axios({
        method: "get",
        url: TOP_RATED_URL,
        params: {
          api_key: API_KEY,
          language: "ko-KR",
        },
      })
        .then((response) => {
          console.log(response)
          context.commit("LOAD_MOVIE_CARDS", response.data.results)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    loadCurrentWeather(context) {
      axios({
        method: "get",
        url: CURRENT_WEATHER_URL,
        params: {
          q: "Seoul",
          appid: OPENWEATHERMAP_API_KEY,
        },
      })
        .then((response) => {
          console.log(response.data.weather[0].description)
          context.commit(
            "LOAD_CURRENT_WEATHER",
            response.data.weather[0].description
          )
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createWatchList(context, title) {
      console.log("ACTIONS!!! __________________________________")
      const watchListItem = {
        title: title,
        isCompleted: false,
      }
      context.commit("CREATE_WATCH_LIST", watchListItem)
      context.dispatch("saveWatchListStorage")
    },
    updatedWatchList(context, list) {
      context.commit("UPDATED_WATCH_LIST", list)
      context.dispatch("saveWatchListStorage")
    },
    saveWatchListStorage(context) {
      const jsonList = JSON.stringify(context.state.watchList)
      localStorage.setItem("list", jsonList)
    },
    loadList(context) {
      context.commit("LOAD_LIST")
    },
    deleteList(context, list) {
      context.commit("DELETE_LIST", list)
      context.dispatch("saveWatchListStorage")
    },
  },
  modules: {},
})
