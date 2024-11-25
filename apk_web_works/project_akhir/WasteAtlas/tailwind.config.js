/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './static/**/*.js'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Georama', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

