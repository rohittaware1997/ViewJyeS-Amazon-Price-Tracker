/** @type {import('jest').Config} */
export default {
  preset: '@quasar/quasar-app-extension-testing-unit-jest',
  // collectCoverage: true,
  // coverageThreshold: {
  //   global: {
  //      branches: 50,
  //      functions: 50,
  //      lines: 50,
  //      statements: 50
  //   },
  // },
  transform: {
    '.*\\.js$': 'babel-jest',
  },
  coveragePathIgnorePatterns: [
    "/node_modules/",
    "/src/boot/firebase.js", // add the path to the file you want to exclude
    "/src/boot/axios.js",
    "/src/pages/",
    "/src/router/",
    "/src/store/",
    "/src/App.vue"
  ]
};
