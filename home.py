{% extends 'baseheader.html' %}

{% block content %}

<div class="container-fluid">

    <div class="row">

        <div class="col-md-12" style="padding-left: 0px;padding-right: 0px;">

            <div class="card border-secondary mb-3">

                <div class="card-body" style="padding: 0px !important;">

                    <img src="{{ welcomepagedata.documentsbanner.url }}" width="100%" height="200px" />

                </div>

            </div>

        </div>

 

    </div>

</div>

<div class="container-fluid text-center" style="padding-left: 0px;padding-right: 0px;padding-bottom: 10px !important;">

    <!-- <div class="card border-secondary mb-3">

        <div class="card-body" style="padding: 0px !important;">

 

            <nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="background-color: #303030 !important;">

                <div class="collapse navbar-collapse" id="navbarSupportedContent">

   

                </div>

            </nav>

        </div>

    </div> -->

    <form class="form-inline my-2 my-lg-0" name="search_form" action="{% url 'searchfiltereddoc' %}" method="GET"

        style="width: 100%;">

        {% csrf_token %}

        <div class="search">

            <input type="text" class="searchTerm" placeholder="Search for document" name="search_box" value="">

            <button type="submit" class="searchButton">

                <i class="fa fa-search"></i>

            </button>

        </div>

    </form>

</div>

<div class="container-fluid">

    <div class="row">

        <div class="col-md-12" style="padding-left: 0px;padding-right: 0px;">

            <div class="card border-secondary mb-3">

                <div class="card-body overflow-auto" style="padding: 0px !important;max-height: calc(100vh - 27rem);">

                    <div id="accordion">

                        {% for documentdict in documents %}

 

                        {% if documentdict %}

                        {% for key,values in documentdict.items %}

                        <!-- collapssible div starts-->

                        <div class="card" style="background-color: transparent;border: none;">

                            <!-- the header portion of the collapsible div starts -->

                            <div class="card-header" id="heading{{ forloop.counter }}"

                                style="border: none !important;background-color: transparent !important;padding: 5px !important;">

 

                                <div class="row" style="margin-left: 0px !important; margin-right: 0px !important">

                                    <div class="col-md-12">

                                        <a class="btn-link" style="text-decoration: none;" href="#"

                                            data-toggle="collapse"

                                            data-target="#collapse{{ forloop.counter }}-{{key|cut:' '}} "

                                            aria-expanded="true" aria-controls="collapse{{ forloop.counter }}">

                                            <h5 style="font-size: 1rem !important; margin-bottom: 0px !important;"><i

                                                    class="fa fa-plus"></i> &nbsp;

                                                {{ key }} ({{values|length}})</h5>

                                        </a>

                                    </div>

                                </div>

                            </div>

                            <!-- the header portion of the collapsible div starts -->

 

                            <!-- the body portion of the collapsible div starts -->

                            <div id="collapse{{ forloop.counter }}-{{key|cut:' '}}" class="collapse hide"

                                aria-labelledby="heading{{ forloop.counter }}">

                                <div class="card-body" id="child{{ forloop.counter }}"

                                    style="padding: 0.2rem !important;margin-left: 1.8rem;">

 

                                    <!-- the inner collapssible div starts-->

                                    {% for document in values %}

                                    <div class="card" style="background-color: transparent;border: none;">

                                        <!-- The header portion of the inner collapssible div starts -->

                                        <div class="card-header accoardian-card-nested-header">

                                            <a class="btn-link" style="text-decoration: none;color:#ffffff !important"

                                                data-toggle="collapse" href="#"

                                                data-target="#collapse{{ document.id }}">

                                                <h5 style="font-size: 1rem !important; margin-bottom: 0px !important;">

                                                    <i class="fas fa-angle-right rotate-icon chevron-style"></i>

                                                    &nbsp;{{ document.title }}

                                                </h5>

                                            </a>

                                        </div>

                                        <!-- The header portion of the inner collapssible div ends -->

 

                                        <!-- The body portion of the inner collapssible div starts -->

                                        <div class="card-body collapse border-secondary nested-card-body"

                                            id="collapse{{ document.id }}">

                                            <div class="container-fluid">

                                                <div class="row">

                                                    {% if document.file_url %}

                                                    <label class="report_item_label">File URL: </label>

                                                    <a href="{{ document.file_url.url }}" style="padding-left: 2px !important;"

                                                        target="_blank">{{ document.title }}</a>

                                                    {% endif %}

                                                    {% if document.published_url %}

                                                    <label class="report_item_label">Published URL: </label>

                                                    <a href="{{ document.published_url }}" style="padding-left: 2px !important;"

                                                        target="_blank">{{ document.title }}</a>

                                                    {% endif %}

                                                </div>

                                                <div class="row">

                                                    <label class="report_item_label">Category: </label>

                                                    <p class="card-text" style="margin-bottom: 0rem !important;padding-left: 2px !important;">

 

                                                        {{ document.document_type }}

                                                    </p>

                                                </div>

                                                <div class="row">

                                                    <div class="col-md-6"

                                                        style="padding-left: 0px !important;width: 50%;">

                                                        <label class="report_item_label">Created By: </label>

                                                       &nbsp; {{ document.created_by}}

                                                    </div>

                                                    <div class="col-md-6" style="width: 50%;">

                                                        <label class="report_item_label">Created On: </label>

                                                        &nbsp;{{ document.created_on}}

                                                    </div>

                                                </div>

                                            </div>

                                        </div>

                                        <!-- The body portion of the iiner collapssible div ends -->

                                    </div>

                                    {% endfor %}

                                    <!-- the inner collapssible div ends -->

                                </div>

                            </div>

                            <!-- the body portion of the collapsible div starts -->

 

                        </div>

                        <!-- collapssible div ends-->

                        {% endfor %}

                        {% endif %}

                        {% endfor %}

                    </div>

                </div>

            </div>

 

            <!-- <div class="card border-secondary mb-3">

                <div class="card-body overflow-auto" style="max-height: calc(100vh - 30rem);">

                    {% for document in documents %}

                    {% if document.file_url %}

                    <a href="{{ document.file_url.url }}" target="_blank">{{ document.title }}</a>

                    {% endif %}

                    {% if document.published_url %}

                    <a href="{{ document.published_url }}" target="_blank">{{ document.title }}</a>

                    {% endif %}

                    <p class="card-text" style="margin-bottom: 0rem !important;">Category: {{ document.document_type }}

                    </p>

                    <div class="container-fluid">

                        <div class="row">

                            <div class="col-md-6" style="padding-left: 0px !important;width: 50%;">

                                <label>Created By: </label> {{ document.created_by}}

                            </div>

                            <div class="col-md-6" style="width: 50%;">

                                <label>Created On: </label> {{ document.created_on}}

                            </div>

                        </div>

                    </div>

                    {% endfor %}

                </div>

            </div> -->

        </div>

    </div>

</div>

<div class="container-fluid text-center" style="padding-left: 0px;">

    <p class="footer-content">{{ welcomepagedata.copyrightmessage }}</p>

</div>

<script>

    $('.btn-link').on('click', function (e) {

        if ($(this).find('h5').find('i').hasClass('fa-angle-right')) {

            $(this).find('.fa-angle-right').removeClass('fa-angle-right').addClass('fa-angle-down');

        } else {

            $(this).find('.fa-angle-down').removeClass('fa-angle-down').addClass('fa-angle-right');

        }

        if ($(this).find('h5').find('i').hasClass('fa-plus')) {

            $(this).find('.fa-plus').removeClass('fa-plus').addClass('fa-minus');

        } else {

            $(this).find('.fa-minus').removeClass('fa-minus').addClass('fa-plus');

        }

    })

</script>

{% endblock content %}