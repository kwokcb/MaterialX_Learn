// UI helpers.

const body = document.body;
// Check if the user has a preferred color scheme
const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

// Set the initial theme based on user preferences
if (prefersDarkMode) {
    console.log('------------- dark mode !')
    body.setAttribute('data-bs-theme', 'dark');
} else {
    console.log('------------- light mode !')
    body.setAttribute('data-bs-theme', 'light');
}
