class Solution {
    public boolean isValid(String s) {
        if(s.length() == 0){
            return true;
        }
        Stack <Character> stack = new Stack<>();
        for(int i=0;i<s.length();i++){
            char x = s.charAt(i);
            if(x=='(' || x=='{' || x=='['){
                stack.push(x);
            }else{
                if(stack.isEmpty()==true)
                return false;
                else if(isMatching(stack.peek(),x) == false)
                return false;
                else
                stack.pop();
            }
        } 
           return (stack.isEmpty()==true);
    }
        public boolean isMatching(char a,char b){
            return ((a=='(' && b==')') || (a=='{' && b=='}') || (a=='[' && b==']'));
        }
}