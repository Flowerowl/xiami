module.export = (location) => {
    let num = location[0];
    let params = location.substr(1, location.length);

    let sliceLength = Math.floor(params.length / num);

    let remainLength = params.length % num;
    let group = [];
    let result = '';

    for (let i=0; i<num; ++i) {
        group[i] = i<remainLength ? params.substr((sliceLength+1)*i, sliceLength+1) : params.substr(sliceLength * (i - remainLength) + (sliceLength + 1) * remainLength, sliceLength);
    }

    for (let i=0; i<group[0].length; ++i) {
        for (let j=0; j<group.length; ++j) {
            result += group[j][i] ? group[j][i] : '';
        }
    }

    return decodeURIComponent(result).replace(/\^/g, '0');
};
