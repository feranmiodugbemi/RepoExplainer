import Ask from './ask.svelte'
import Github from './github.svelte'


const routes = [
    {
        name : '/',
        component : Github
    },
    {
        name : '/ask',
        component : Ask
    }
]

export {routes}