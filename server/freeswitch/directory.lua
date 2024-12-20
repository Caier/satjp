function genUser(i)
    return [[
        <user id="]] .. i .. [[">
    <params>
      <param name="password" value="]] .. freeswitch.getGlobalVariable("default_password") .. [["/>
      <param name="vm-password" value="1001"/>
    </params>
    <variables>
      <variable name="toll_allow" value="domestic,international,local"/>
      <variable name="accountcode" value="]] .. i .. [["/>
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension ]] .. i .. [["/>
      <variable name="effective_caller_id_number" value="]] .. i .. [["/>
      <variable name="outbound_caller_id_name" value="]] .. freeswitch.getGlobalVariable("outbound_caller_name") .. [["/>
      <variable name="outbound_caller_id_number" value="]] .. freeswitch.getGlobalVariable("outbound_caller_id") .. [["/>
      <variable name="callgroup" value="techsupport"/>
        </variables>
        </user>
    ]]
end

testusers = ""
legacyusers = ""

for i=10000,13000 do
    testusers = testusers .. genUser(i)
end

for i=1000,1019 do
    legacyusers = legacyusers .. genUser(i)
end


directory = [[
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="freeswitch/xml">
  <section name="directory" description="directory">
    <domain name="]].. freeswitch.getGlobalVariable("domain") ..[[">
        <params>
        <param name="dial-string" value="{^^:sip_invite_domain=${dialed_domain}:presence_id=${dialed_user}@${dialed_domain}}${sofia_contact(*/${dialed_user}@${dialed_domain})},${verto_contact(${dialed_user}@${dialed_domain})}"/>
        <!-- These are required for Verto to function properly -->
        <param name="jsonrpc-allowed-methods" value="verto"/>
        <!-- <param name="jsonrpc-allowed-event-channels" value="demo,conference,presence"/> -->
        </params>

        <variables>
        <variable name="record_stereo" value="true"/>
        <variable name="default_gateway" value="]] .. freeswitch.getGlobalVariable("default_provider") .. [["/>
        <variable name="default_areacode" value="]] .. freeswitch.getGlobalVariable("default_areacode") .. [["/>
        <variable name="transfer_fallback_extension" value="operator"/>
        </variables>

        <groups>
        <group name="default">
        <users>
          ]] .. legacyusers .. testusers .. [[
        </users>
        </group>
        </groups>
    </domain>
  </section>
</document>
]]

XML_STRING = directory
-- freeswitch.consoleLog("notice", "Debug XML:\n" .. XML_STRING .. "\n")    