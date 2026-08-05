# -*- coding: utf-8 -*-
import os
import re

file_path = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

vocab_dict = {
    'International Olympic Committee': '(n) /ˌɪn.təˈnæʃ.ən.əl əˈlɪm.pɪk kəˈmɪt.i/',
    "World's Fair": '(n) /ˌwɜːldz ˈfeər/',
    'agriculture': '(n) /ˈæɡ.rɪ.kʌl.tʃər/',
    'altitude sickness': '(n) /ˈæl.tɪ.tjuːd ˌsɪk.nəs/',
    'ancient': '(adj) /ˈeɪn.ʃənt/',
    'ancient Mesoamerica': '(n) /ˈeɪn.ʃənt ˌmez.oʊ.əˈmer.ɪ.kə/',
    'ancient microbial life': '(n) /ˈeɪn.ʃənt maɪˈkroʊ.bi.əl laɪf/',
    'antibiotics': '(n) /ˌæn.ti.baɪˈɒt.ɪks/',
    'aplastic anemia': '(n) /eɪˌplæs.tɪk əˈniː.mi.ə/',
    'architectural feats': '(n) /ˌɑː.kɪˈtek.tʃər.əl fiːts/',
    'asylum': '(n) /əˈsaɪ.ləm/',
    'athletes': '(n) /ˈæθ.liːts/',
    'attracts': '(v) /əˈtrækts/',
    'attributed to': '(v) /əˈtrɪb.juːt.ɪd tuː/',
    'avalanches': '(n) /ˈæv.ə.lɑːnʃɪz/',
    'beloved symbol': '(n) /bɪˈlʌv.ɪd ˈsɪm.bəl/',
    'beverage': '(n) /ˈbev.ər.ɪdʒ/',
    'biodiversity': '(n) /ˌbaɪ.oʊ.daɪˈvɜː.sə.ti/',
    'bitter': '(adj) /ˈbɪt.ər/',
    'by accident': '(adv) /baɪ ˈæk.sɪ.dənt/',
    'candidate': '(n) /ˈkæn.dɪ.dət/',
    'carbon footprint': '(n) /ˌkɑː.bən ˈfʊt.prɪnt/',
    'casualties': '(n) /ˈkæʒ.ju.əl.tiz/',
    'cattle ranching': '(n) /ˈkæt.əl ˌrɑːn.tʃɪŋ/',
    'cognitive development': '(n) /ˈkɒɡ.nə.tɪv dɪˈvel.əp.mənt/',
    'colonization': '(n) /ˌkɒl.ə.naɪˈzeɪ.ʃən/',
    'commuters': '(n) /kəˈmjuː.tərz/',
    'competing': '(v) /kəmˈpiː.tɪŋ/',
    'complex social behavior': '(n) /ˈkɒm.pleks ˈsoʊ.ʃəl bɪˈheɪ.vjər/',
    'consequences': '(n) /ˈkɒn.sɪ.kwənsɪz/',
    'consumed': '(v) /kənˈsjuːmd/',
    'countless': '(adj) /ˈkaʊnt.ləs/',
    'creative ways': '(n) /kriˈeɪ.tɪv weɪz/',
    'cultural icon': '(n) /ˈkʌl.tʃər.əl ˈaɪ.kɒn/',
    'currency': '(n) /ˈkʌr.ən.si/',
    'deeply': '(adv) /ˈdiːp.li/',
    'deforestation': '(n) /diːˌfɒr.ɪˈsteɪ.ʃən/',
    'digital age': '(n) /ˈdɪdʒ.ɪ.təl eɪdʒ/',
    'elevation': '(n) /ˌel.ɪˈveɪ.ʃən/',
    'entrance arch': '(n) /ˈen.trəns ɑːtʃ/',
    'eyesore': '(n) /ˈaɪ.sɔːr/',
    'fascinated by': '(adj) /ˈfæs.ɪ.neɪ.tɪd baɪ/',
    'featured': '(v) /ˈfiː.tʃərd/',
    'flavor': '(n) /ˈfleɪ.vər/',
    'fosters': '(v) /ˈfɒs.tərz/',
    'founded': '(v) /ˈfaʊn.dɪd/',
    'fresh produce': '(n) /freʃ ˈprɒd.juːs/',
    'frothy drink': '(n) /ˈfrɒθ.i drɪŋk/',
    'government': '(n) /ˈɡʌv.ən.mənt/',
    'harsh weather': '(n) /hɑːʃ ˈweð.ər/',
    'iceberg': '(n) /ˈaɪs.bɜːɡ/',
    'identified as': '(v) /aɪˈden.tɪ.faɪd æz/',
    'increasingly popular': '(adj) /ɪnˈkriː.sɪŋ.li ˈpɒp.jə.lər/',
    'influencing': '(v) /ˈɪn.flu.əns.ɪŋ/',
    'influential figures': '(n) /ˌɪn.fluˈen.ʃəl ˈfɪɡ.ərz/',
    'inspire': '(v) /ɪnˈspaɪər/',
    'inspired by': '(adj) /ɪnˈspaɪərd baɪ/',
    'intelligence': '(n) /ɪnˈtel.ɪ.dʒəns/',
    'interactions': '(n) /ˌɪn.təˈræk.ʃənz/',
    'laboratory analysis': '(n) /ləˈbɒr.ə.tər.i əˈnæl.ə.sɪs/',
    'laid the foundation': '(v) /leɪd ðə faʊnˈdeɪ.ʃən/',
    'launched': '(v) /lɔːntʃt/',
    'legacy': '(n) /ˈleɡ.ə.si/',
    'maiden voyage': '(n) /ˈmeɪ.dən ˈvɔɪ.ɪdʒ/',
    'manually': '(adv) /ˈmæn.ju.ə.li/',
    'maritime disaster': '(n) /ˈmær.ɪ.taɪm dɪˈzɑː.stər/',
    'massive': '(adj) /ˈmæs.ɪv/',
    'masterpiece': '(n) /ˈmɑː.stə.piːs/',
    'measures': '(n) /ˈmeʒ.ərz/',
    'meeting places': '(n) /ˈmiː.tɪŋ ˌpleɪs.ɪz/',
    'mirrors': '(n) /ˈmɪr.ərz/',
    'modern technology': '(n) /ˈmɒd.ən tekˈnɒl.ə.dʒi/',
    'mold': '(n) /moʊld/',
    'mountaineers': '(n) /ˌmaʊn.tɪˈnɪərz/',
    'myth': '(n) /mɪθ/',
    'naked eye': '(n) /ˌneɪ.kɪd ˈaɪ/',
    'nomadic invasions': '(n) /noʊˈmæd.ɪk ɪnˈveɪ.ʒənz/',
    'numerous': '(adj) /ˈnjuː.mə.rəs/',
    'operating': '(v) /ˈɒp.ər.eɪ.tɪŋ/',
    'originally built': '(v) /əˈrɪdʒ.ɪ.nəl.i bɪlt/',
    'passenger': '(n) /ˈpæs.ən.dʒər/',
    'passenger liner': '(n) /ˈpæs.ən.dʒər ˈlaɪ.nər/',
    'patrols': '(n) /pəˈtroʊlz/',
    'petri dish': '(n) /ˈpet.ri ˌdɪʃ/',
    'pioneering': '(adj) /ˌpaɪəˈnɪə.rɪŋ/',
    'pods': '(n) /pɒdz/',
    'posthumous fame': '(n) /ˈpɒs.tʃə.məs feɪm/',
    'poverty': '(n) /ˈpɒv.ə.ti/',
    'process': '(v) /ˈproʊ.ses/',
    'productivity': '(n) /ˌprɒd.ʌkˈtɪv.ə.ti/',
    'professionals': '(n) /prəˈfeʃ.ən.əlz/',
    'prolonged exposure': '(n) /prəˈlɒŋd ɪkˈspoʊ.ʒər/',
    'public transport': '(n) /ˈpʌb.lɪk ˈtræns.pɔːt/',
    'radiation': '(n) /ˌreɪ.diˈeɪ.ʃən/',
    'radioactivity': '(n) /ˌreɪ.di.oʊ.ækˈtɪv.ə.ti/',
    'rainforest': '(n) /ˈreɪn.fɒr.ɪst/',
    'recognizable': '(adj) /ˈrek.əɡ.naɪ.zə.bəl/',
    'recognize': '(v) /ˈrek.əɡ.naɪz/',
    'referred to as': '(v) /rɪˈfɜːrd tuː æz/',
    'remarkable': '(adj) /rɪˈmɑː.kə.bəl/',
    'remeasured': '(v) /ˌriːˈmeʒ.ərd/',
    'rich history': '(n) /rɪtʃ ˈhɪs.tər.i/',
    'ritual': '(n) /ˈrɪtʃ.u.əl/',
    'routes': '(n) /ruːts/',
    'rover': '(n) /ˈroʊ.vər/',
    'scientific fields': '(n) /ˌsaɪənˈtɪf.ɪk fiːldz/',
    'sense of community': '(n) /sens əv kəˈmjuː.nə.ti/',
    'severe mental illness': '(n) /sɪˈvɪər ˈmen.təl ˈɪl.nəs/',
    'severe threats': '(n) /sɪˈvɪər θrets/',
    'significant role': '(n) /sɪɡˈnɪf.ɪ.kənt roʊl/',
    'solve problems': '(v) /sɒlv ˈprɒb.ləmz/',
    'species': '(n) /ˈspiː.ʃiːz/',
    'striking': '(v) /ˈstraɪ.kɪŋ/',
    'structure': '(n) /ˈstrʌk.tʃər/',
    'sufficient lifeboats': '(n) /səˈfɪʃ.ənt ˈlaɪf.boʊts/',
    'sustainable living': '(n) /səˈsteɪ.nə.bəl ˈlɪv.ɪŋ/',
    'trait': '(n) /treɪt/',
    'transforming': '(v) /trænsˈfɔːm.ɪŋ/',
    'urban farming': '(n) /ˈɜː.bən ˈfɑː.mɪŋ/',
    'variety': '(n) /vəˈraɪ.ə.ti/',
    'via': '(prep) /ˈvaɪ.ə/',
    'vital role': '(n) /ˈvaɪ.təl roʊl/'
}

def replace_match(match):
    word = match.group(1)
    meaning = match.group(2)
    if word in vocab_dict:
        pronunciation = vocab_dict[word]
        # Replace the item with pronunciation injected
        return f'<li><strong>{word}</strong> <span style="color: #64748b; font-size: 0.9rem; margin-left: 4px; font-weight: 500;">{pronunciation}</span>: {meaning}</li>'
    return match.group(0)

# Replace all occurrences
new_content = re.sub(r'<li><strong>(.*?)</strong>:\s*(.*?)</li>', replace_match, content)

# Check how many were replaced
print("Total words replaced:", sum(1 for word in re.findall(r'<li><strong>(.*?)</strong> <span', new_content)))

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
