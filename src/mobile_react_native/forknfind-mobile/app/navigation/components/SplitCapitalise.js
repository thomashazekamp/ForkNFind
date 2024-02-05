function SplitCapitalise(sentence){

    const words = sentence.split('_');

    const finishedWords = words.map(word => {
        const capitalise = word.charAt(0).toUpperCase();
        const normal = word.slice(1).toLowerCase();

        return capitalise + normal;
    });

    return finishedWords.join(' ')
}

export default SplitCapitalise;