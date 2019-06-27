# test file for git
 the common context
 ~ change file for update
 ~ change file for update2 
VMware Workstation Pro


*Master and Feature1 branch add context dev issue*


**git bash 退出vim，按Esc退出输入模式，然后按shift + ; ,再输入q!或wq! (wq!是保存退出，q!是直接退出)**

<https://www.crifan.com/emulate_login_example_for_analysis_and_write_code_for_emulate_upload_file/>


[idea 安装和破解](https://www.cnblogs.com/jpfss/p/8872358.html)<br />

<https://www.cnblogs.com/zyl910/p/java_war_properties_path_easy.html>

<https://blog.csdn.net/laoyang360>


```java
   public ListNode insertionSortList(ListNode head) {
        if(head == null || head.ext == null){
            return;
        }
        
        ListNode l = new ListNode(-1);
        l.next = head;
        ListNode prev = head;
        
        ListNode node;
        ListNode iter;
        ListNode iterPrev;
        while(prev.next != null){
            node = prev.next;
            prev.next = node.next;
            iter = head;
            iterPrev = l;
            while(iter != prev){
                if(iter.val > node.val) break;
                iter = iter.next;
                iterPrev = iter;
            }
            
            iterPrev.next = node;
            node.next = iter;
        }
        return l.next;
    }
```
