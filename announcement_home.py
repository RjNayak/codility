{% extends 'baseheader.html' % }

{% block content % }

<div class = "container-fluid" >

   <div class = "row" >

        <div class = "col-md-12" style = "padding-left: 0px;padding-right: 0px;" >

           <div class = "card border-secondary mb-3" >

                <div class = "card-body" style = "padding: 0px !important;" >

                    <img src = "{{ welcomepagedata.announcementbanner.url }}" width = "100%" height = "200px" / >

                </div >

            </div >

        </div >

    </div >

</div >

<div class = "container-fluid" >

   <div class = "row" >

        <div class = "col-md-12" style = "padding-left: 0px;padding-right: 0px;">

           <div class = "card border-secondary mb-3" >

                <div class = "card-header" style = "border-color: #6c757d!important;">

                    <div class = "row" style = "padding: 0px !important;">

                        <div class = "col-md-10" > <b><span

                            style = "white-space: nowrap;" > Announcements</span></b></div>

                        <div class = "col-md-2" style = "text-align: end !important;">

                            <input id = "toggle-one" checked type = "checkbox" data-height='15'>

                        </div >

                    </div >

                </div >

                <div class = "card-body overflow-auto" id = "active_announcement" style="max-height: calc(100vh - 30rem);">


                    { % if announcements % }


                   { % for announcement in announcements % }

                    { % if today < announcement.expiration_date.date  % }

                    <div class = "row" >

                       <div class = "col-md-12" >

                            <h5 class = "card-title report_item_label" style = "margin-bottom: 0rem !important;">

                                { % if announcement.announcement_type.name == 'Announcement' % }

                                <i class = "fa fa-bullhorn" > </i>

                                { % endif % }

                                { % if announcement.announcement_type.name == 'Notification' % }

                                <i class = "fa fa-bell" > </i>

                                { % endif % }

                                {{announcement.title }} < /h5 >

                        </div >

                    </div >

                    <div class = "row" style = "margin-left: 5px;">

                       <div class = "col-md-12" >

                            <p class = "card-text" style = "margin-bottom: 0rem !important;">{{ announcement.description }}

                            </p >

                            { % if announcement.file_url % }

                            <a href = "{{ announcement.file_url.url }}" target = "_blank">{{ announcement.file_url}}</a>

                            { % endif % }

                            { % if announcement.information_url % }

                            <a href = "{{ announcement.information_url }}"

                                target = "_blank" > {{ announcement.information_url}}</a>

                            { % endif % }

                            <p class = "card-text" > Announced On: {{ announcement.announcement_date }}</p>

                        </div >

                    </div >

                    { % else%}



                    { % endif % }

                    { % endfor % }



                    { % else% }
                    <h5 class = "card-title" > No active announcements</h5>


                    { % endif % }
 

                    

                </div >

                <div class = "card-body overflow-auto" id = "archived_announcement" style="max-height: calc(100vh - 30rem);">

                    { % for announcement in announcements % }

                    <div class = "row" >

                       <div class = "col-md-12" >

                            <h5 class = "card-title report_item_label" style = "margin-bottom: 0rem !important;">

                                { % if announcement.announcement_type.name == 'Announcement' % }

                                <i class = "fa fa-bullhorn" > </i>

                                { % endif % }

                                { % if announcement.announcement_type.name == 'Notification' % }

                                <i class = "fa fa-bell" > </i>

                                { % endif % }

                                {{announcement.title }} < /h5 >

                        </div >

                    </div >

                    <div class = "row" style = "margin-left: 5px;">

                       <div class = "col-md-12" >

                            <p class = "card-text" style = "margin-bottom: 0rem !important;">{{ announcement.description }}

                            </p >

                            { % if announcement.file_url % }

                            <a href = "{{ announcement.file_url.url }}" target = "_blank">{{ announcement.file_url}}</a>

                            { % endif % }

                            { % if announcement.information_url % }

                            <a href = "{{ announcement.information_url }}"

                                target = "_blank" > {{ announcement.information_url}}</a>

                            { % endif % }

                            <div >

                                <p class = "card-text float-left" > Announced On: {{ announcement.announcement_date }} </p>

                                <p class = "card-text float-right" > Expired On: {{ announcement.expiration_date }}</p>

                            </div >

                        </div >

                    </div >

                    { % endfor % }

                </div >

            </div >

        </div >

    </div >

</div >

<div class = "container-fluid text-center" style = "padding-left: 0px;">

    <p class = "footer-content" > {{ welcomepagedata.copyrightmessage }}</p>


</div >

<script >

   $(function () {$('#toggle-one').bootstrapToggle({

        on: 'Active',

        off: 'Archived'

    })

        $('#archived_announcement').hide()

        $('#active_announcement').show()

        $('#toggle-one').change(function() {$('#active_announcement').toggle()

                                            $('#archived_announcement').toggle()

                                            })

    })

</script >

<style >

.toggle-on {

     background-color:  # FFEB3B !important;

     color: black !important

     border-color: # FFFFFF !important;

     }

 .toggle-off {

      background-color:  # FFEB3B !important;

      color: black !important

      border-color: # FFFFFF !important;

      }

  .toggle-handle {

       color:  # FFFFFF !important;

        background-color: # FFFFFF !important;

       }

   .toggle,

    .toggle-on,

    .toggle-off {

        border-radius: 20px !important

    }

    .toggle .toggle-handle {

        border-radius: 20px !important

    }

</style >

{ % endblock content % }
