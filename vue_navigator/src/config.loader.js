function getConfigValue(key) {
  let value = '';
  if (process.env && process.env[`${key}`] !== undefined) {
    // get env var value
    value = process.env[`${key}`];
  } else {
    // get value from meta tag
    return getMetaValue(key);
  }
  return value;
}

/**
 * Get value from HTML meta tag
 */
function getMetaValue(key) {
  let value = '';
  const node = document.querySelector(`meta[property=${key}]`);
  if (node !== null) {
    value = node.getAttribute('content');
  }
  return value;
}

export default { getConfigValue, getMetaValue };