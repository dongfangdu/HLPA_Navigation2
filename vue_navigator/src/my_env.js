import axios from 'axios'

const myEnv = axios.create({
    other_ip: process.env.VUE_APP_OTHER_IP,
});

export default myEnv;