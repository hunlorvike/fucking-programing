function lengthOfLongestSubstring(s: string): number {
    const subString = new Set<string>();
    let answer = 0;
    let start = 0;
    for (let index = 0; index < s.length; index++) {
        const char = s[index];
        while (subString.has(char)) {
            subString.delete(s[start]);
            start++;
        }
        subString.add(char);
        answer = Math.max(answer, index - start + 1);
    }
    return answer;
}
