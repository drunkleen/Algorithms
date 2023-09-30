public class BinarySearchRecursive {
    public static void main(String[] args){
        int[] numberList = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73};
        int numToFind = 57;
        System.out.println("Index of number " + numToFind + " is: "+ birarySearchRecursive(numToFind, numberList));
    }

private static int birarySearchRecursive(int numberToFind ,int[] numbers) {
    return birarySearchRecursive(numberToFind, numbers, 0, numbers.length);
}

private static int birarySearchRecursive(int numberToFind, int[] numbers, int firstIndex, int lastIndex) {
    if (lastIndex >= firstIndex && firstIndex < numbers.length - 1) {
        int middleIndex = firstIndex + (lastIndex - firstIndex) / 2;
        int middleNumber = numbers[middleIndex];

        if (numberToFind == middleNumber) {
            return middleIndex;
        }

        if (numberToFind < middleNumber) {
            return birarySearchRecursive(numberToFind, numbers, firstIndex, middleIndex - 1);
        } else {
            return birarySearchRecursive(numberToFind, numbers, middleIndex + 1, lastIndex);
        }
    }
    return -1;
}

}
