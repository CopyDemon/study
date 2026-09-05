/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "app/api/login/route";
exports.ids = ["app/api/login/route"];
exports.modules = {

/***/ "next/dist/compiled/next-server/app-page.runtime.dev.js":
/*!*************************************************************************!*\
  !*** external "next/dist/compiled/next-server/app-page.runtime.dev.js" ***!
  \*************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/compiled/next-server/app-page.runtime.dev.js");

/***/ }),

/***/ "next/dist/compiled/next-server/app-route.runtime.dev.js":
/*!**************************************************************************!*\
  !*** external "next/dist/compiled/next-server/app-route.runtime.dev.js" ***!
  \**************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/compiled/next-server/app-route.runtime.dev.js");

/***/ }),

/***/ "../app-render/work-async-storage.external":
/*!*****************************************************************************!*\
  !*** external "next/dist/server/app-render/work-async-storage.external.js" ***!
  \*****************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/server/app-render/work-async-storage.external.js");

/***/ }),

/***/ "./work-unit-async-storage.external":
/*!**********************************************************************************!*\
  !*** external "next/dist/server/app-render/work-unit-async-storage.external.js" ***!
  \**********************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/server/app-render/work-unit-async-storage.external.js");

/***/ }),

/***/ "(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Flogin%2Froute&page=%2Fapi%2Flogin%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Flogin%2Froute.ts&appDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice%2Fsrc%2Fapp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!":
/*!***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Flogin%2Froute&page=%2Fapi%2Flogin%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Flogin%2Froute.ts&appDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice%2Fsrc%2Fapp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D! ***!
  \***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   patchFetch: () => (/* binding */ patchFetch),\n/* harmony export */   routeModule: () => (/* binding */ routeModule),\n/* harmony export */   serverHooks: () => (/* binding */ serverHooks),\n/* harmony export */   workAsyncStorage: () => (/* binding */ workAsyncStorage),\n/* harmony export */   workUnitAsyncStorage: () => (/* binding */ workUnitAsyncStorage)\n/* harmony export */ });\n/* harmony import */ var next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/dist/server/route-modules/app-route/module.compiled */ \"(rsc)/./node_modules/next/dist/server/route-modules/app-route/module.compiled.js\");\n/* harmony import */ var next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_dist_server_route_kind__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/dist/server/route-kind */ \"(rsc)/./node_modules/next/dist/server/route-kind.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/dist/server/lib/patch-fetch */ \"(rsc)/./node_modules/next/dist/server/lib/patch-fetch.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var _Users_shengpang_Desktop_self_dev_learn_study_JS_nextjs_nextjs_with_sql_practice_src_app_api_login_route_ts__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./src/app/api/login/route.ts */ \"(rsc)/./src/app/api/login/route.ts\");\n\n\n\n\n// We inject the nextConfigOutput here so that we can use them in the route\n// module.\nconst nextConfigOutput = \"\"\nconst routeModule = new next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__.AppRouteRouteModule({\n    definition: {\n        kind: next_dist_server_route_kind__WEBPACK_IMPORTED_MODULE_1__.RouteKind.APP_ROUTE,\n        page: \"/api/login/route\",\n        pathname: \"/api/login\",\n        filename: \"route\",\n        bundlePath: \"app/api/login/route\"\n    },\n    resolvedPagePath: \"/Users/shengpang/Desktop/self/dev/learn/study/JS/nextjs/nextjs-with-sql-practice/src/app/api/login/route.ts\",\n    nextConfigOutput,\n    userland: _Users_shengpang_Desktop_self_dev_learn_study_JS_nextjs_nextjs_with_sql_practice_src_app_api_login_route_ts__WEBPACK_IMPORTED_MODULE_3__\n});\n// Pull out the exports that we need to expose from the module. This should\n// be eliminated when we've moved the other routes to the new format. These\n// are used to hook into the route.\nconst { workAsyncStorage, workUnitAsyncStorage, serverHooks } = routeModule;\nfunction patchFetch() {\n    return (0,next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__.patchFetch)({\n        workAsyncStorage,\n        workUnitAsyncStorage\n    });\n}\n\n\n//# sourceMappingURL=app-route.js.map//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9ub2RlX21vZHVsZXMvbmV4dC9kaXN0L2J1aWxkL3dlYnBhY2svbG9hZGVycy9uZXh0LWFwcC1sb2FkZXIvaW5kZXguanM/bmFtZT1hcHAlMkZhcGklMkZsb2dpbiUyRnJvdXRlJnBhZ2U9JTJGYXBpJTJGbG9naW4lMkZyb3V0ZSZhcHBQYXRocz0mcGFnZVBhdGg9cHJpdmF0ZS1uZXh0LWFwcC1kaXIlMkZhcGklMkZsb2dpbiUyRnJvdXRlLnRzJmFwcERpcj0lMkZVc2VycyUyRnNoZW5ncGFuZyUyRkRlc2t0b3AlMkZzZWxmJTJGZGV2JTJGbGVhcm4lMkZzdHVkeSUyRkpTJTJGbmV4dGpzJTJGbmV4dGpzLXdpdGgtc3FsLXByYWN0aWNlJTJGc3JjJTJGYXBwJnBhZ2VFeHRlbnNpb25zPXRzeCZwYWdlRXh0ZW5zaW9ucz10cyZwYWdlRXh0ZW5zaW9ucz1qc3gmcGFnZUV4dGVuc2lvbnM9anMmcm9vdERpcj0lMkZVc2VycyUyRnNoZW5ncGFuZyUyRkRlc2t0b3AlMkZzZWxmJTJGZGV2JTJGbGVhcm4lMkZzdHVkeSUyRkpTJTJGbmV4dGpzJTJGbmV4dGpzLXdpdGgtc3FsLXByYWN0aWNlJmlzRGV2PXRydWUmdHNjb25maWdQYXRoPXRzY29uZmlnLmpzb24mYmFzZVBhdGg9JmFzc2V0UHJlZml4PSZuZXh0Q29uZmlnT3V0cHV0PSZwcmVmZXJyZWRSZWdpb249Jm1pZGRsZXdhcmVDb25maWc9ZTMwJTNEISIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7OztBQUErRjtBQUN2QztBQUNxQjtBQUMyRDtBQUN4STtBQUNBO0FBQ0E7QUFDQSx3QkFBd0IseUdBQW1CO0FBQzNDO0FBQ0EsY0FBYyxrRUFBUztBQUN2QjtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBO0FBQ0EsWUFBWTtBQUNaLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxRQUFRLHNEQUFzRDtBQUM5RDtBQUNBLFdBQVcsNEVBQVc7QUFDdEI7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUMwRjs7QUFFMUYiLCJzb3VyY2VzIjpbIiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBBcHBSb3V0ZVJvdXRlTW9kdWxlIH0gZnJvbSBcIm5leHQvZGlzdC9zZXJ2ZXIvcm91dGUtbW9kdWxlcy9hcHAtcm91dGUvbW9kdWxlLmNvbXBpbGVkXCI7XG5pbXBvcnQgeyBSb3V0ZUtpbmQgfSBmcm9tIFwibmV4dC9kaXN0L3NlcnZlci9yb3V0ZS1raW5kXCI7XG5pbXBvcnQgeyBwYXRjaEZldGNoIGFzIF9wYXRjaEZldGNoIH0gZnJvbSBcIm5leHQvZGlzdC9zZXJ2ZXIvbGliL3BhdGNoLWZldGNoXCI7XG5pbXBvcnQgKiBhcyB1c2VybGFuZCBmcm9tIFwiL1VzZXJzL3NoZW5ncGFuZy9EZXNrdG9wL3NlbGYvZGV2L2xlYXJuL3N0dWR5L0pTL25leHRqcy9uZXh0anMtd2l0aC1zcWwtcHJhY3RpY2Uvc3JjL2FwcC9hcGkvbG9naW4vcm91dGUudHNcIjtcbi8vIFdlIGluamVjdCB0aGUgbmV4dENvbmZpZ091dHB1dCBoZXJlIHNvIHRoYXQgd2UgY2FuIHVzZSB0aGVtIGluIHRoZSByb3V0ZVxuLy8gbW9kdWxlLlxuY29uc3QgbmV4dENvbmZpZ091dHB1dCA9IFwiXCJcbmNvbnN0IHJvdXRlTW9kdWxlID0gbmV3IEFwcFJvdXRlUm91dGVNb2R1bGUoe1xuICAgIGRlZmluaXRpb246IHtcbiAgICAgICAga2luZDogUm91dGVLaW5kLkFQUF9ST1VURSxcbiAgICAgICAgcGFnZTogXCIvYXBpL2xvZ2luL3JvdXRlXCIsXG4gICAgICAgIHBhdGhuYW1lOiBcIi9hcGkvbG9naW5cIixcbiAgICAgICAgZmlsZW5hbWU6IFwicm91dGVcIixcbiAgICAgICAgYnVuZGxlUGF0aDogXCJhcHAvYXBpL2xvZ2luL3JvdXRlXCJcbiAgICB9LFxuICAgIHJlc29sdmVkUGFnZVBhdGg6IFwiL1VzZXJzL3NoZW5ncGFuZy9EZXNrdG9wL3NlbGYvZGV2L2xlYXJuL3N0dWR5L0pTL25leHRqcy9uZXh0anMtd2l0aC1zcWwtcHJhY3RpY2Uvc3JjL2FwcC9hcGkvbG9naW4vcm91dGUudHNcIixcbiAgICBuZXh0Q29uZmlnT3V0cHV0LFxuICAgIHVzZXJsYW5kXG59KTtcbi8vIFB1bGwgb3V0IHRoZSBleHBvcnRzIHRoYXQgd2UgbmVlZCB0byBleHBvc2UgZnJvbSB0aGUgbW9kdWxlLiBUaGlzIHNob3VsZFxuLy8gYmUgZWxpbWluYXRlZCB3aGVuIHdlJ3ZlIG1vdmVkIHRoZSBvdGhlciByb3V0ZXMgdG8gdGhlIG5ldyBmb3JtYXQuIFRoZXNlXG4vLyBhcmUgdXNlZCB0byBob29rIGludG8gdGhlIHJvdXRlLlxuY29uc3QgeyB3b3JrQXN5bmNTdG9yYWdlLCB3b3JrVW5pdEFzeW5jU3RvcmFnZSwgc2VydmVySG9va3MgfSA9IHJvdXRlTW9kdWxlO1xuZnVuY3Rpb24gcGF0Y2hGZXRjaCgpIHtcbiAgICByZXR1cm4gX3BhdGNoRmV0Y2goe1xuICAgICAgICB3b3JrQXN5bmNTdG9yYWdlLFxuICAgICAgICB3b3JrVW5pdEFzeW5jU3RvcmFnZVxuICAgIH0pO1xufVxuZXhwb3J0IHsgcm91dGVNb2R1bGUsIHdvcmtBc3luY1N0b3JhZ2UsIHdvcmtVbml0QXN5bmNTdG9yYWdlLCBzZXJ2ZXJIb29rcywgcGF0Y2hGZXRjaCwgIH07XG5cbi8vIyBzb3VyY2VNYXBwaW5nVVJMPWFwcC1yb3V0ZS5qcy5tYXAiXSwibmFtZXMiOltdLCJpZ25vcmVMaXN0IjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Flogin%2Froute&page=%2Fapi%2Flogin%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Flogin%2Froute.ts&appDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice%2Fsrc%2Fapp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!\n");

/***/ }),

/***/ "(rsc)/./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true!":
/*!******************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true! ***!
  \******************************************************************************************************/
/***/ (() => {



/***/ }),

/***/ "(ssr)/./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true!":
/*!******************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true! ***!
  \******************************************************************************************************/
/***/ (() => {



/***/ }),

/***/ "(rsc)/./src/app/api/login/get.ts":
/*!**********************************!*\
  !*** ./src/app/api/login/get.ts ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   GET: () => (/* binding */ GET)\n/* harmony export */ });\n/* harmony import */ var next_server__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/server */ \"(rsc)/./node_modules/next/dist/api/server.js\");\n\n/**\n * TODO: remove this api later, no need for GET request for login api\n * @description GET request for login api, now use for test api\n * @param request NextRequest\n * @returns response\n */ async function GET(request) {\n    return next_server__WEBPACK_IMPORTED_MODULE_0__.NextResponse.json({\n        message: \"Are you try to login?\"\n    });\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9zcmMvYXBwL2FwaS9sb2dpbi9nZXQudHMiLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBd0Q7QUFFeEQ7Ozs7O0NBS0MsR0FDTSxlQUFlQyxJQUFJQyxPQUFvQjtJQUMxQyxPQUFPRixxREFBWUEsQ0FBQ0csSUFBSSxDQUFDO1FBQUVDLFNBQVM7SUFBd0I7QUFDaEUiLCJzb3VyY2VzIjpbIi9Vc2Vycy9zaGVuZ3BhbmcvRGVza3RvcC9zZWxmL2Rldi9sZWFybi9zdHVkeS9KUy9uZXh0anMvbmV4dGpzLXdpdGgtc3FsLXByYWN0aWNlL3NyYy9hcHAvYXBpL2xvZ2luL2dldC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBOZXh0UmVxdWVzdCwgTmV4dFJlc3BvbnNlIH0gZnJvbSBcIm5leHQvc2VydmVyXCI7XG5cbi8qKlxuICogVE9ETzogcmVtb3ZlIHRoaXMgYXBpIGxhdGVyLCBubyBuZWVkIGZvciBHRVQgcmVxdWVzdCBmb3IgbG9naW4gYXBpXG4gKiBAZGVzY3JpcHRpb24gR0VUIHJlcXVlc3QgZm9yIGxvZ2luIGFwaSwgbm93IHVzZSBmb3IgdGVzdCBhcGlcbiAqIEBwYXJhbSByZXF1ZXN0IE5leHRSZXF1ZXN0XG4gKiBAcmV0dXJucyByZXNwb25zZVxuICovXG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gR0VUKHJlcXVlc3Q6IE5leHRSZXF1ZXN0KSB7XG4gICAgcmV0dXJuIE5leHRSZXNwb25zZS5qc29uKHsgbWVzc2FnZTogXCJBcmUgeW91IHRyeSB0byBsb2dpbj9cIiB9KTtcbn1cbiJdLCJuYW1lcyI6WyJOZXh0UmVzcG9uc2UiLCJHRVQiLCJyZXF1ZXN0IiwianNvbiIsIm1lc3NhZ2UiXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(rsc)/./src/app/api/login/get.ts\n");

/***/ }),

/***/ "(rsc)/./src/app/api/login/post.ts":
/*!***********************************!*\
  !*** ./src/app/api/login/post.ts ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   POST: () => (/* binding */ POST)\n/* harmony export */ });\n/* harmony import */ var next_server__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/server */ \"(rsc)/./node_modules/next/dist/api/server.js\");\n\nasync function POST(request) {\n    console.log(`login post request`);\n    const body = await request.json();\n    const username = body.username;\n    const password = body.password;\n    // simulate login authentication query from db and find valid user\n    if (username === 'asd' && password === 'asd') {\n        //simulate login process generate a web token\n        let webToken = \"allow\";\n        // simulate setup auto logout after 60 seconds\n        setTimeout(()=>{\n            webToken = \"\";\n            console.log(`post request done`);\n        }, 60000);\n        return next_server__WEBPACK_IMPORTED_MODULE_0__.NextResponse.json({\n            message: `successful login with uname: ${username} and pwd: ${password}`,\n            webToken\n        });\n    }\n    // TODO: can check username is wrong or password is wrong or all wrong\n    // simulate invalid username or password\n    if (username !== 'asd' || password !== 'asd') {\n        return next_server__WEBPACK_IMPORTED_MODULE_0__.NextResponse.json({\n            message: \"Invalid username or password\"\n        }, {\n            status: 401\n        });\n    }\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9zcmMvYXBwL2FwaS9sb2dpbi9wb3N0LnRzIiwibWFwcGluZ3MiOiI7Ozs7O0FBQXdEO0FBQ2pELGVBQWVDLEtBQUtDLE9BQW9CO0lBQzNDQyxRQUFRQyxHQUFHLENBQUMsQ0FBQyxrQkFBa0IsQ0FBQztJQUVoQyxNQUFNQyxPQUFPLE1BQU1ILFFBQVFJLElBQUk7SUFDL0IsTUFBTUMsV0FBV0YsS0FBS0UsUUFBUTtJQUM5QixNQUFNQyxXQUFXSCxLQUFLRyxRQUFRO0lBRTlCLGtFQUFrRTtJQUNsRSxJQUFHRCxhQUFhLFNBQVNDLGFBQWEsT0FBTztRQUN6Qyw2Q0FBNkM7UUFDN0MsSUFBSUMsV0FBVztRQUVmLDhDQUE4QztRQUM5Q0MsV0FBVztZQUNQRCxXQUFXO1lBQ1hOLFFBQVFDLEdBQUcsQ0FBQyxDQUFDLGlCQUFpQixDQUFDO1FBQ25DLEdBQUc7UUFFSCxPQUFPSixxREFBWUEsQ0FBQ00sSUFBSSxDQUFDO1lBQ3JCSyxTQUFTLENBQUMsNkJBQTZCLEVBQUVKLFNBQVMsVUFBVSxFQUFFQyxVQUFVO1lBQ3hFQztRQUNKO0lBQ0o7SUFFQSxzRUFBc0U7SUFDdEUsd0NBQXdDO0lBQ3hDLElBQUdGLGFBQWEsU0FBU0MsYUFBYSxPQUFPO1FBQ3pDLE9BQU9SLHFEQUFZQSxDQUFDTSxJQUFJLENBQ3BCO1lBQUVLLFNBQVM7UUFBK0IsR0FDMUM7WUFBRUMsUUFBUTtRQUFJO0lBRXRCO0FBQ0oiLCJzb3VyY2VzIjpbIi9Vc2Vycy9zaGVuZ3BhbmcvRGVza3RvcC9zZWxmL2Rldi9sZWFybi9zdHVkeS9KUy9uZXh0anMvbmV4dGpzLXdpdGgtc3FsLXByYWN0aWNlL3NyYy9hcHAvYXBpL2xvZ2luL3Bvc3QudHMiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgTmV4dFJlcXVlc3QsIE5leHRSZXNwb25zZSB9IGZyb20gXCJuZXh0L3NlcnZlclwiO1xuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIFBPU1QocmVxdWVzdDogTmV4dFJlcXVlc3QpIHtcbiAgICBjb25zb2xlLmxvZyhgbG9naW4gcG9zdCByZXF1ZXN0YClcblxuICAgIGNvbnN0IGJvZHkgPSBhd2FpdCByZXF1ZXN0Lmpzb24oKTtcbiAgICBjb25zdCB1c2VybmFtZSA9IGJvZHkudXNlcm5hbWU7XG4gICAgY29uc3QgcGFzc3dvcmQgPSBib2R5LnBhc3N3b3JkO1xuXG4gICAgLy8gc2ltdWxhdGUgbG9naW4gYXV0aGVudGljYXRpb24gcXVlcnkgZnJvbSBkYiBhbmQgZmluZCB2YWxpZCB1c2VyXG4gICAgaWYodXNlcm5hbWUgPT09ICdhc2QnICYmIHBhc3N3b3JkID09PSAnYXNkJykge1xuICAgICAgICAvL3NpbXVsYXRlIGxvZ2luIHByb2Nlc3MgZ2VuZXJhdGUgYSB3ZWIgdG9rZW5cbiAgICAgICAgbGV0IHdlYlRva2VuID0gXCJhbGxvd1wiOyBcblxuICAgICAgICAvLyBzaW11bGF0ZSBzZXR1cCBhdXRvIGxvZ291dCBhZnRlciA2MCBzZWNvbmRzXG4gICAgICAgIHNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgICAgICAgd2ViVG9rZW4gPSBcIlwiO1xuICAgICAgICAgICAgY29uc29sZS5sb2coYHBvc3QgcmVxdWVzdCBkb25lYClcbiAgICAgICAgfSwgNjAwMDApXG5cbiAgICAgICAgcmV0dXJuIE5leHRSZXNwb25zZS5qc29uKHsgXG4gICAgICAgICAgICBtZXNzYWdlOiBgc3VjY2Vzc2Z1bCBsb2dpbiB3aXRoIHVuYW1lOiAke3VzZXJuYW1lfSBhbmQgcHdkOiAke3Bhc3N3b3JkfWAgLFxuICAgICAgICAgICAgd2ViVG9rZW4gLy8gd2ViIHRva2VuIGZvciBhdXRoZW50aWNhdGlvblxuICAgICAgICB9KTtcbiAgICB9XG5cbiAgICAvLyBUT0RPOiBjYW4gY2hlY2sgdXNlcm5hbWUgaXMgd3Jvbmcgb3IgcGFzc3dvcmQgaXMgd3Jvbmcgb3IgYWxsIHdyb25nXG4gICAgLy8gc2ltdWxhdGUgaW52YWxpZCB1c2VybmFtZSBvciBwYXNzd29yZFxuICAgIGlmKHVzZXJuYW1lICE9PSAnYXNkJyB8fCBwYXNzd29yZCAhPT0gJ2FzZCcpIHtcbiAgICAgICAgcmV0dXJuIE5leHRSZXNwb25zZS5qc29uKFxuICAgICAgICAgICAgeyBtZXNzYWdlOiBcIkludmFsaWQgdXNlcm5hbWUgb3IgcGFzc3dvcmRcIiB9LFxuICAgICAgICAgICAgeyBzdGF0dXM6IDQwMSB9LCBcbiAgICAgICAgKTtcbiAgICB9XG59XG4iXSwibmFtZXMiOlsiTmV4dFJlc3BvbnNlIiwiUE9TVCIsInJlcXVlc3QiLCJjb25zb2xlIiwibG9nIiwiYm9keSIsImpzb24iLCJ1c2VybmFtZSIsInBhc3N3b3JkIiwid2ViVG9rZW4iLCJzZXRUaW1lb3V0IiwibWVzc2FnZSIsInN0YXR1cyJdLCJpZ25vcmVMaXN0IjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(rsc)/./src/app/api/login/post.ts\n");

/***/ }),

/***/ "(rsc)/./src/app/api/login/route.ts":
/*!************************************!*\
  !*** ./src/app/api/login/route.ts ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   GET: () => (/* reexport safe */ _get__WEBPACK_IMPORTED_MODULE_0__.GET),\n/* harmony export */   POST: () => (/* reexport safe */ _post__WEBPACK_IMPORTED_MODULE_1__.POST)\n/* harmony export */ });\n/* harmony import */ var _get__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./get */ \"(rsc)/./src/app/api/login/get.ts\");\n/* harmony import */ var _post__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./post */ \"(rsc)/./src/app/api/login/post.ts\");\n\n\n/**\n * GET: test api\n * POST: login api\n */ \n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9zcmMvYXBwL2FwaS9sb2dpbi9yb3V0ZS50cyIsIm1hcHBpbmdzIjoiOzs7Ozs7O0FBQTRCO0FBQ0U7QUFFOUI7OztDQUdDLEdBQ29CIiwic291cmNlcyI6WyIvVXNlcnMvc2hlbmdwYW5nL0Rlc2t0b3Avc2VsZi9kZXYvbGVhcm4vc3R1ZHkvSlMvbmV4dGpzL25leHRqcy13aXRoLXNxbC1wcmFjdGljZS9zcmMvYXBwL2FwaS9sb2dpbi9yb3V0ZS50cyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBHRVQgfSBmcm9tIFwiLi9nZXRcIjtcbmltcG9ydCB7IFBPU1QgfSBmcm9tIFwiLi9wb3N0XCI7XG5cbi8qKlxuICogR0VUOiB0ZXN0IGFwaVxuICogUE9TVDogbG9naW4gYXBpXG4gKi9cbmV4cG9ydCB7IEdFVCwgUE9TVCB9OyJdLCJuYW1lcyI6WyJHRVQiLCJQT1NUIl0sImlnbm9yZUxpc3QiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(rsc)/./src/app/api/login/route.ts\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, ["vendor-chunks/next"], () => (__webpack_exec__("(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Flogin%2Froute&page=%2Fapi%2Flogin%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Flogin%2Froute.ts&appDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice%2Fsrc%2Fapp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=%2FUsers%2Fshengpang%2FDesktop%2Fself%2Fdev%2Flearn%2Fstudy%2FJS%2Fnextjs%2Fnextjs-with-sql-practice&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!")));
module.exports = __webpack_exports__;

})();