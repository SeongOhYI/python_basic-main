hits_text = "심장혈관 막는 '제로'?…기자가 직접 파헤쳐 봤더니 (자막뉴스) / SBS 게시자: SBS 뉴스 6일 전 2분 15초 조회수 970,746회"

# 해당 텍스트의 마지막 인덱스로 부터 조회수 라는 글자가 있는 인덱스 값을 가져옴
print(hits_text.rfind("조회수")) 
print(hits_text.rfind("조회수")+4)
start_index = hits_text.rfind("조회수")+4
end_index = hits_text.rfind("회")
print(hits_text[start_index:end_index]) # 970,746
hits = hits_text[start_index:end_index] # 970,746
hits = int(hits.replace(",", "")) # 970746
print(hits) # 970746