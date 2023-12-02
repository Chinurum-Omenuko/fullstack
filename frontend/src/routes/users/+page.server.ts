
/** @type {import('./$types').PageServerLoad} */
export const load = async () => {
    const res = await fetch('http://127.0.0.1:8000/users')
    const user_info = await res.json()
    return { user_info }
    
    

}