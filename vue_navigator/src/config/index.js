import loader from '../config.loader';

export default {
    VUE_APP_DEPLOY_HOST: loader.getConfigValue('VUE_APP_DEPLOY_HOST'),
    VUE_APP_DEPLOY_PORT: loader.getConfigValue('VUE_APP_DEPLOY_PORT'),
    VUE_APP_DEPLOY_URL: 'http://' + loader.getConfigValue('VUE_APP_DEPLOY_HOST') + ":" + loader.getConfigValue('VUE_APP_DEPLOY_PORT'),
    BASE_URL: loader.getConfigValue('BASE_URL'),
};
