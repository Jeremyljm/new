#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

text = """
<li class="con_list_item default_list" data-index="1" data-positionid="5821804" data-salary="15k-25k" data-company="阿博茨科技" data-positionname="PYTHON开发工程师 (MJ000126)" data-companyid="129068" data-hrid="9945455" data-tpladword="0">
        
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/5821804.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="
                
                    
                    0102
                    
                
                " data-lg-tj-cid="5821804" data-lg-tj-abt="dm-csearch-useLayeredDisplay|0">
                        <h3 style="max-width: 180px;">PYTHON开发工程师 (MJ000126)</h3>
                        
                            
                                
                                    <span class="add">[<em>北京·学院路</em>]</span>
                                
                            
                        

                    </a>
                    <span class="format-time">1天前发布</span>
                             
                        
                            <input type="hidden" class="hr_portrait" value="i/image3/M00/23/C5/Cgq2xlqWGl-AEwmcAAHBfUyrETc496.jpg">
                            <input type="hidden" class="hr_name" value="Cathy">
                            <input type="hidden" class="hr_position" value="HRBP">
                            <input type="hidden" class="target_hr" value="9945455">
                            <input type="hidden" class="target_position" value="5821804">
                            
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0102" data-lg-tj-cid="129068" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            
                        
                    
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-25k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/129068.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                
                    
                    0102
                    
                
                " data-lg-tj-cid="129068" data-lg-tj-abt="dm-csearch-useLayeredDisplay|0">阿博茨科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网 / B轮 / 150-500人
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/129068.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="               
                    0102
                
                " data-lg-tj-cid="129068" data-lg-tj-abt="dm-csearch-useLayeredDisplay|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/54/CA/CgpFT1mBnPCAN1lSAABwbgtCYF4746.jpg" alt="阿博茨科技" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            
                <div class="li_b_l">
                    
                        <span>移动互联网</span>
                    
                        <span>Python</span>
                    
                </div>
            
            <div class="li_b_r">“金融科技 人工智能”</div>
        </div>
    </li>
"""


# html = etree.HTML(text)
# print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

def parse_text():
    html = etree.HTML(text)
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

def parse_file():
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse("lagou.html",parser=parser)
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_text()