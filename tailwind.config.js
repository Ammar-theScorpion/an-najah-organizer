/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

module.exports = {
  content: ["./an_najah_organizer/templates/**/*.{html,js}", "./an_najah_organizer/templates/rooms/*.{html,js}"],
  theme: {
    colors: {
      white: colors.white,
      black: colors.black,
      cfe: "#007cae",
      cfeBlue: {
        100: "#007cad"
      },
      stone: colors.stone,
      sky: colors.sky,
      violet: colors.violet,
    },
    extend: {},
  },
  plugins: [],
}
